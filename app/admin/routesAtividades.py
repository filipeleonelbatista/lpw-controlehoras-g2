from flask import render_template, redirect, request, url_for, flash
from flask_table import Table
from .formsAtividades import AtividadeForm, Results
from . import admin

@admin.route('/admin/atividades', methods=['GET', 'POST'])
def atividades():
	form = AtividadeForm()
	results = []
	table = Results(results)
	return render_template('admin/atividades.html', form=form, table=table)
