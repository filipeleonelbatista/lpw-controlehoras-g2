from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required
from .formsFuncionarios import FuncionarioForm
from . import admin
from app.models import User
from app import db

@admin.route('/admin/funcionarios', methods=['GET', 'POST'])
@login_required
def funcionarios():
	form = FuncionarioForm()
	if request.method == 'POST' and form.salvar.data == True:
		try:
			user = User(matricula=form.matricula.data, username=form.nome.data, password=form.password.data, is_admin=form.admin.data)
			db.session.add(user)
			db.session.commit()
			flash('Registrado com sucesso', 'success')
		except:
			db.session.rollback()
			flash('Registro falhou na adição', 'danger')
			
	elif request.method == 'GET' and request.args.get('delete'):
		try:
			user = User.query.filter_by(matricula=request.args.get('delete')).first_or_404()
			db.session.delete(user)
			db.session.commit()
			flash('Registro apagado com sucesso', 'danger')
		except:
			db.session.rollback()
			flash('Registro falhou em apagar', 'danger')

	elif request.method == 'GET' and request.args.get('update'):
		user = User.query.filter_by(matricula=request.args.get('update')).first_or_404()
		form.matricula.data = user.matricula
		form.nome.data = user.username
		form.admin.data = user.is_admin
		return render_template('admin/editFuncionario.html',form=form, action='funcUpdate')

	listTable=User.query.all()
	return render_template('admin/funcionarios.html', form=form, listTable=listTable)

@admin.route('/admin/funcUpdate', methods=['GET', 'POST'])
@login_required
def funcUpdate():
	form = FuncionarioForm()
	if request.method == 'POST' and form.salvar.data == True:
		user = User.query.filter_by(matricula=form.matricula.data).first_or_404()
		if user:
			user.username = form.nome.data
			user.matricula = form.matricula.data
			user.is_admin = form.admin.data
			user.password_hash = form.password.data
			try:
				db.session.commit()
				flash('Registro alterado com sucesso', 'info')
			except:
				db.session.rollback()
				flash('Registro falhou em alterar', 'danger')
	return redirect(url_for('.funcionarios'))
