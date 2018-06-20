from flask import render_template, redirect, request, url_for, flash
from .forms import RelatForm, Results
from . import dashaboard

@dashaboard.route('/dashaboard/horastrabalhadas', methods=['GET', 'POST'])
def horastrabalhadas():
	return render_template('dashaboard/ht.html')
