from flask import render_template, redirect, request, url_for, flash
from flask_table import Table
from .formsProjetos import ProjetoForm, Results
from . import admin

@admin.route('/admin/projetos', methods=['GET', 'POST'])
def projetos():
	form = ProjetoForm()
	results = []
	table = Results(results)
	return render_template('admin/projetos.html', form=form, table=table)
