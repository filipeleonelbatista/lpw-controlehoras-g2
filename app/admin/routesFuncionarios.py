from flask import render_template, redirect, request, url_for, flash
from flask_table import Table
from .formsFuncionarios import FuncionarioForm, Results
from . import admin

@admin.route('/admin/funcionarios', methods=['GET', 'POST'])
def funcionarios():
	form = FuncionarioForm()
	results = []
	table = Results(results)
	form.nome.data='Lucio'
	form.matricula.data=896
	table.nome.data='Felipe'
	table.matr.data=123
	return render_template('admin/funcionarios.html', form=form, table=table)
