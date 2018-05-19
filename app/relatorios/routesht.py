from flask import render_template, redirect, request, url_for, flash
from .forms import RelatForm, Results
from . import relatorios

@relatorios.route('/relatorios/horastrabalhadas', methods=['GET', 'POST'])
def horastrabalhadas():
	return render_template('relatorios/ht.html')
