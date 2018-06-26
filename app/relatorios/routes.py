import calendar, datetime
import locale
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user
from .forms import horasProjetoForm
from . import relatorios
from app.models import Task, Project, Lancamento, Binding

@relatorios.route('/horasPorProjeto', methods=['GET', 'POST'])
@login_required
def horasProjeto():
	hpform = horasProjetoForm()
	hpform.selectProject.choices = [(project.project_id, project.project.nameProject) \
		for project in Binding.query.filter_by(users_id=current_user.id).all()]


	months_choices = []
	locale.setlocale(locale.LC_ALL, 'pt_PT.UTF-8')
	for i in range(1,13):
		months_choices.append((i, datetime.date(2018, i, 1).strftime('%B')))
	hpform.selectMonth.choices = months_choices

	listTable=Lancamento.query.all()
	return render_template('relatorios/horasPorProjeto.html', listTable=listTable, hpform=hpform)
