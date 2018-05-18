from flask import render_template, redirect, request, url_for, flash
from flask_table import Table
from .formsVinculacao import VincForm, Results
from . import admin

@admin.route('/admin/vinculcao', methods=['GET', 'POST'])
def vinculcao():
	form = VincForm()
	results = []
	table = Results(results)
	return render_template('admin/vinculcao.html', form=form, table=table)
