from flask import render_template, redirect, request, url_for, flash
from flask_table import Table
from .formsFuncionarios import FuncionarioForm, Results
from . import admin

@admin.route('/admin/funcionarios', methods=['GET', 'POST'])
def funcionarios():
	form = FuncionarioForm()
	results = []
	table = Results(results)
	return render_template('admin/funcionarios.html', form=form, table=table)
