from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required
from . import lancamentos
from .formLancamentos import lancamentoForm
from app import db
from app.models import Task, Project, Lancamento

@lancamentos.route('/lancamentos', methods=['GET', 'POST'])
@login_required
def lancamentos():
	form = lancamentoForm()
	form.selectProjeto.choices = [(project.id, project.nameProject) for project in Project.getAllProject()]
	form.selectAtividade.choices = [(task.codTask, task.descricao) for task in Task.getAllTask()]
	if request.method == 'POST' and form.iniciar.data == True:
		print("depois post")
		try:
			if form.validacao(form):
				flash('Falta preenchar um campo!', 'danger')
			else:
				print(form.selectProjeto.data)
				print(form.dtInicio.data)
				print(form.hrInicio.data)
				print(form.dtFim.data)
				print(form.hrFim.data)
				print(form.selectAtividade.data)
				print(form.descricao.data)
				lancamento = Lancamento(
					project_id=form.selectProjeto.data,
					dtInic=form.dtInicio.data,
					hrInic=form.hrInicio.data,
					dtFim=form.dtFim.data,
					hrFim=form.hrFim.data,
					task_id=form.selectAtividade.data,
					descricao=form.descricao.data
					)
				print("commit")
				db.session.add(lancamento)
				db.session.commit()
				flash('Registrado com sucesso', 'success')
		except:
			db.session.rollback()
			flash('Registro falhou na adição', 'danger')
			
	elif request.method == 'GET' and request.args.get('delete'):
		try:
			if request.args.get('delete') == '':
				flash('Falta a matricula!', 'danger')
			else:				
				db.session.delete(user)
				db.session.commit()
				flash('Registro apagado com sucesso', 'danger')
		except:
			db.session.rollback()
			flash('Registro falhou em apagar', 'danger')

	elif request.method == 'GET' and request.args.get('update'):
		if request.args.get('update') == '':
			flash('Falta a matricula!', 'danger')
		else:
			return render_template('lancamentos/editLancamentos.html',form=form, action='lancUpdate')

	listTable=Lancamento.query.all()
	for item in listTable:
		print(item)
	return render_template('lancamentos/lancamentos.html', form=form, listTable=listTable)
