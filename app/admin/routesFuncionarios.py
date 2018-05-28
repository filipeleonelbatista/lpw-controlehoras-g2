from flask import render_template, redirect, request, url_for, flash
from flask_table import Table
from .formsFuncionarios import FuncionarioForm
from . import admin
from app.models import User
from app import db

@admin.route('/admin/funcionarios', methods=['GET', 'POST'])
def funcionarios():
	form = FuncionarioForm()
	if form.validate_on_submit():
		user = User(matricula=form.matricula.data, username=form.nome.data, password=form.password.data, is_admin=form.admin.data)
		db.session.add(user)
		db.session.commit()
	

	if request.method == 'GET' and request.args.get('delete'):
		user = User.query.filter_by(matricula=request.args.get('delete')).first()
		db.session.delete(user)
		db.session.commit()

	listTable=User.query.all()
	return render_template('admin/funcionarios.html', form=form, listTable=listTable)
	
