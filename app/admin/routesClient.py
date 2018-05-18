from flask import render_template, redirect, request, url_for, flash
from flask_table import Table
from .formsClient import ClientsForm, Results
from . import admin

@admin.route('/admin/clientes', methods=['GET', 'POST'])
def clientes():
	form = ClientsForm()
	results = []
	table = Results(results)
	return render_template('admin/clientes.html', form=form, table=table)
