import calendar, datetime
from sqlalchemy import extract
#import locale
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user
from .forms import horasProjetoForm
from . import relatorios
from app.models import Task, Project, Lancamento, Binding

@relatorios.route('/horasPorProjeto', methods=['GET', 'POST'])
@login_required
def horasProjeto():
	hpform = horasProjetoForm()
	projtChoices=[]
	projtChoices.append((0, ''))
	for project in Binding.query.filter_by(users_id=current_user.id).all():
		projtChoices.append((project.project_id, project.project.nameProject))
	hpform.selectProject.choices = projtChoices

	months_choices = []
	months_choices.append((0, ''))
	#locale.setlocale(locale.LC_ALL, 'pt_PT.UTF-8')
	mesP = ['', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
	for i in range(1,13):
		months_choices.append((i, mesP[i]))
	hpform.selectMonth.choices = months_choices

	if request.method == 'POST' and hpform.gravar.data == True:
		print('value')
		listTable = Lancamento.query.filter_by(users_id=current_user.id).all()
		if hpform.selectProject.data != '0':
			print('projeto' + hpform.selectProject.data)
			selectProj=hpform.selectProject.data
			listTable = Lancamento.query.filter_by(users_id=current_user.id, project_id=selectProj).all()
		if hpform.selectMonth.data != '0':
			print('mes')
			selectMon=hpform.selectMonth.data
			listTable = Lancamento.query.filter_by(users_id=current_user.id).filter(extract('month', Lancamento.dtInic) == selectMon).order_by(Lancamento.id.desc()).all()
			if hpform.selectMonth.data != '0' and hpform.selectProject.data != '0':
				listTable = Lancamento.query.filter_by(users_id=current_user.id, project_id=selectProj).filter(extract('month', Lancamento.dtInic) == selectMon).order_by(Lancamento.id.desc()).all()
		return render_template('relatorios/horasPorProjeto.html', listTable=listTable, hpform=hpform)
	else:
		pass

	users=Binding.query.filter_by(users_id=current_user.id).all()
	print(users)
	for user in users:
		if user.is_coord:
			print('Coordenador')
			listTable=Lancamento.query.filter_by(project_id=user.project_id).all()
			return render_template('relatorios/horasPorProjeto.html', listTable=listTable, hpform=hpform)

	listTable = Lancamento.query.filter_by(users_id=current_user.id).all()
	return render_template('relatorios/horasPorProjeto.html', listTable=listTable, hpform=hpform)
