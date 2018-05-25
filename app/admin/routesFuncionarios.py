from flask import render_template, redirect, request, url_for, flash
from flask_table import Table
from .formsFuncionarios import FuncionarioForm
from . import admin
from app.models import User
from app import db

@admin.route('/admin/funcionarios', methods=['GET', 'POST'])
def funcionarios():
	form = FuncionarioForm()
	print(form.salvar)
	if request.method == 'POST' and form.salvar.id == "salvar":
		user = User(matricula=form.matricula.data, username=form.nome.data, password=form.password.data, is_admin=form.admin.data)
		db.session.add(user)
		db.session.commit()

	if request.method == 'GET' and request.args.get('delete'):
		print(request.args.get('delete'))
		user = User.query.filter_by(matricula=request.args.get('delete')).first()
		db.session.delete(user)
		db.session.commit()

	if request.method == 'GET' and request.args.get('update'):
		print(request.args.get('update'))
		user = User.query.filter_by(matricula=request.args.get('update')).first()
		print(user.username)
		form.matricula.data = user.matricula
		form.nome.data = user.username
		form.admin.data = user.is_admin
		return render_template('admin/edit.html',form=form)

	listTable=User.query.all()
	return render_template('admin/funcionarios.html', form=form, listTable=listTable)

@admin.route('/admin/funcUpdate', methods=['GET', 'POST'])
def funcUpdate():
	form = FuncionarioForm()
	if request.method == 'POST' and form.salvar.id == "salvar":
		user = User.query.filter_by(matricula=form.matricula.data).first()
		if user:
			print ('OK')
			user.username = form.nome.data
			user.matricula = form.matricula.data
			user.is_admin = form.admin.data
			user.password_hash = form.password.data
			db.session.commit()

	listTable=User.query.all()
	return render_template('admin/funcionarios.html', form=form, listTable=listTable)