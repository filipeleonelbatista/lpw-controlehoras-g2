from flask import render_template, redirect, request, url_for, flash
from .forms import RelatForm, Results
from . import relatorios

@relatorios.route('/relatorios/horasxprojeto', methods=['GET', 'POST'])
def horasxprojeto():
	return render_template('relatorios/hxp.html')