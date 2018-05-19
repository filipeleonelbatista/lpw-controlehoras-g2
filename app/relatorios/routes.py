from flask import render_template, redirect, request, url_for, flash
from .forms import RelatForm, Results
from . import relatorios

@relatorios.route('/relatorios', methods=['GET', 'POST'])
def relatorios():
	form = RelatForm()
	results = []
	table = Results(results)
	return render_template('relatorios/relatorios.html', form=form, table=table)

