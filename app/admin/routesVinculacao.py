from flask import render_template, redirect, request, url_for, flash
from flask_table import Table
from .formsVinculacao import VincForm, Results
from . import admin

@admin.route('/admin/vinculacao', methods=['GET', 'POST'])
def vinculacao():
	form = VincForm()
	results = []
	table = Results(results)
	return render_template('admin/vinculacao.html', form=form, table=table)
