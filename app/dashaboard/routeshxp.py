from flask import render_template, redirect, request, url_for, flash
from .forms import RelatForm, Results
from . import dashaboard

@dashaboard.route('/dashaboard/horasxprojeto', methods=['GET', 'POST'])
def horasxprojeto():
	return render_template('dashaboard/hxp.html')