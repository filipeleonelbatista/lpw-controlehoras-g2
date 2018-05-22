from flask import render_template, redirect, request, url_for, flash
from flask_table import Table
from .formsFuncionarios import FuncionarioForm, Results
from . import admin
from app.models import User

@admin.route('/admin/funcionarios', methods=['GET', 'POST'])
def funcionarios():
	form = FuncionarioForm()
	results = []
	table = Results(results)
	if request.method == 'POST':
		print('Aqui')
	
	listTable=User.query.all()	
	return render_template('admin/funcionarios.html', form=form, table=listTable)
