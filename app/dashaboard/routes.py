from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required
from .forms import RelatForm, Results
from . import dashaboard

@dashaboard.route('/', methods=['GET', 'POST'])
@dashaboard.route('/dashaboard', methods=['GET', 'POST'])
@login_required
def dashaboard():
	form = RelatForm()
	results = []
	table = Results(results)
	return render_template('dashaboard/dashaboard.html', form=form, table=table)

