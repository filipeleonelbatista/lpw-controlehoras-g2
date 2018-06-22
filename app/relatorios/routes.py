from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required
from .forms import horasProjetoForm, Results
from . import relatorios
from app.models import Task, Project, Lancamento

@relatorios.route('/horasPorProjeto', methods=['GET', 'POST'])
@login_required
def horasProjeto():
	hpform = horasProjetoForm()
	hpform.selectProject.choices = [(project.id, project.nameProject) for project in Project.getAllProject()]
	hpform.selectMonth.choices = [(lancamento.id, lancamento.dtInic) for lancamento in Lancamento.getAllLancamento()]


	listTable=Lancamento.query.all()
	return render_template('relatorios/horasPorProjeto.html', listTable=listTable, hpform=hpform)
