import os
from werkzeug.utils import secure_filename

from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash
from app import db
from app.models import User
from .forms import PerfilForm
from . import perfil

ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])
UPLOAD_FOLDER = 'app/static/images/'

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@perfil.route('/perfil', methods=['GET', 'POST'])
@login_required
def perfil():
	form = PerfilForm()
	if request.method == 'POST' and form.submit.data == True:
		if form.password.data != form.confirm.data:
			flash('Senha são diferentes!', 'danger')
		elif form.validacao(form):
			flash('Campo vazio!', 'danger')
		elif form.validlengthPass(form):
			flash('Senha tem tamanho minimo de 4 caracteres', 'danger')
		else:
			user = User.query.filter_by(matricula=form.matricula.data).first_or_404()
			print(user.fullusername)
			if user:
				user.fullusername = form.nomeCompleto.data
				user.username = form.nome.data
				user.matricula = form.matricula.data
				user.password_hash = generate_password_hash(form.password.data)
				try:
					db.session.add(user)
					db.session.commit()
					flash('Registro alterado com sucesso', 'success')
				except:
					db.session.rollback()
					flash('Registro falhou em alterar', 'danger')
			else:
				print('Usuario nao foi encontrado e/ou nao existe')
	elif request.method == 'POST' and form.enviar.data == True:
		file = request.files['upload']
		if file and allowed_file(file.filename):
			user = User.query.filter_by(matricula=current_user.matricula).first_or_404()
			file.save(os.path.join(UPLOAD_FOLDER, file.filename))
			user.imagem = file.filename
			try:
				db.session.commit()
				flash('Registro alterado com sucesso', 'info')
			except:
				db.session.rollback()
				flash('Registro falhou em alterar', 'danger')
		else:
			flash('Não foi selecionado nenhum arquivo ou não existe', 'danger')
		
		
	user = User.query.filter_by(matricula=current_user.matricula).first_or_404()
	form.matricula.data = user.matricula
	form.nome.data = user.username
	form.nomeCompleto.data = user.fullusername
	return render_template('perfil/perfil.html', form=form, avatar=user.imagem)
