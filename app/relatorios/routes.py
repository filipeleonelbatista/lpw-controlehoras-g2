from datetime import timedelta, datetime
from sqlalchemy import extract
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
			for user in listTable:
				dateBegin = datetime(user.dtInic.year, user.dtInic.month, user.dtInic.day, user.hrInic.hour, user.hrInic.minute, user.hrInic.second)
				dateEnd = datetime(user.dtInic.year, user.dtInic.month, user.dtInic.day, user.hrFim.hour, user.hrFim.minute, user.hrFim.second)
				somaDateHora = datetime(1, 1, 1, 0, 0)
				somaDateHora = somaDateHora + (dateEnd - dateBegin)
			return render_template('relatorios/horasPorProjeto.html', listTable=listTable, hpform=hpform, somaDateHora=somaDateHora)

	listTable = Lancamento.query.filter_by(users_id=current_user.id).all()
	print('value')
	for user in listTable:
		print('value')
		dateBegin = datetime(user.dtInic.year, user.dtInic.month, user.dtInic.day, user.hrInic.data.hour, user.hrInic.data.minute, user.hrInic.data.second)
		dateEnd = datetime(user.dtInic.year, user.dtInic.month, user.dtInic.day, user.hrFim.data.hour, user.hrFim.data.minute, user.hrFim.data.second)
		somaDateHora = somaDateHora + (dateEnd - dateBegin)
	return render_template('relatorios/horasPorProjeto.html', listTable=listTable, hpform=hpform, somaDateHora=somaDateHora)
