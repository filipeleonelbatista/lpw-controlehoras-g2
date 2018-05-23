from flask import render_template, redirect, request, url_for, flash
from flask_table import Table
from .formsFuncionarios import FuncionarioForm, Results
from . import admin
from app import db
from app.models import User

@admin.route('/admin/funcionarios', methods=['GET', 'POST'])
def funcionarios():
	form = FuncionarioForm()
	if form.validate_on_submit() and form.salvar.data:
		user = User(matricula=form.matricula.data, username=form.nome.data, password=form.password.data, is_admin=form.admin.data)
		print('User: [%s]' % user.username)
    	#db.session.add(user)
    	#db.session.commit()
    	    	
	listTable=User.query.all()	
	return render_template('admin/funcionarios.html', form=form, listTable=listTable)
