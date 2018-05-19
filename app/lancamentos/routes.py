from flask import render_template, redirect, request, url_for, flash
from flask_table import Table
from . import lancamentos

@lancamentos.route('/lancamentos', methods=['GET', 'POST'])
def lancamentos():
	return render_template('lancamentos/lancamentos.html')
