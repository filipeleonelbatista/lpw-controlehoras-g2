from flask import render_template, redirect, request, url_for, flash
from .forms import RelatForm, Results
from . import dashaboard

@dashaboard.route('/dashaboard', methods=['GET', 'POST'])
def dashaboard():
	form = RelatForm()
	results = []
	table = Results(results)
	return render_template('dashaboard/dashaboard.html', form=form, table=table)

