from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required
from .forms import RelatForm, Results
from . import relatorios
from app.models import Task, Project, Lancamento


@relatorios.route('/minhasHoras', methods=['GET', 'POST'])
@login_required
def minhasHoras():
	listTable=Lancamento.query.all()
	return render_template('relatorios/minhasHoras.html', listTable=listTable)

@relatorios.route('/horasPorProjeto', methods=['GET', 'POST'])
@login_required
def horasProjeto():
	listTable=Lancamento.query.all()
	return render_template('relatorios/horasPorProjeto.html', listTable=listTable)
