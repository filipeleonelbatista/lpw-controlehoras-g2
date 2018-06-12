from flask import render_template, redirect, request, url_for, flash
from . import lancamentos
from .formLancamentos import lancamentoForm
from .formLancamentos import relogioForm
from app.models import Task, Project

@lancamentos.route('/lancamentos', methods=['GET', 'POST'])
def lancamentos():
	form = lancamentoForm()
	form.selectProjeto.choices = [(project.id, project.nameProject) for project in Project.getAllProject()]
	form.selectAtividade.choices = [(task.codTask, task.descricao) for task in Task.getAllTask()]
	formR = relogioForm()

	if formR.iniciar.data:
		# iniciar o contador e jogar a hora inicial no campo data/hora
		pass
	
	if formR.parar.data:
		# parar o contador jogar a hora final no campo data/hora
		pass

	if formR.gravar.data:
		# gravar todos os dados e jogar na tabela.
		pass
		

	#listTable=User.query.all()listTable=listTable
	return render_template('lancamentos/lancamentos.html', form=form, formR=formR)

