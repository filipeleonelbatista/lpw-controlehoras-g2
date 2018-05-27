from flask import render_template, redirect, request, url_for, flash
from .formsAtividades import AtividadeForm
from . import admin
from app.models import Task
from app import db

@admin.route('/admin/atividades', methods=['GET', 'POST'])
def atividades():
	form = AtividadeForm()
	if request.method == 'POST' and form.salvar.id == "salvar":
		try:
			print(form.idAtividade.data)
			print(form.descricao.data)
			atividade = Task(codTask=form.idAtividade.data, descricao=form.descricao.data)
			db.session.add(atividade)
			db.session.commit()
			flash('Registrado com sucesso', 'success')
		except:
			db.session.rollback()
			flash('Registro falhou na adição', 'danger')

	elif request.method == 'GET' and request.args.get('delete'):
		try:
			atividade = Task.query.filter_by(codTask=request.args.get('delete')).first_or_404()
			db.session.delete(atividade)
			db.session.commit()
			flash('Registro apagado com sucesso', 'danger')
		except:
			db.session.rollback()
			flash('Registro falhou em apagar', 'danger')

	elif request.method == 'GET' and request.args.get('update'):
		atividade = Task.query.filter_by(codTask=request.args.get('update')).first_or_404()
		form.idAtividade.data = atividade.codTask
		form.descricao.data = atividade.descricao
		return render_template('admin/editAtividade.html',form=form, action='atividUpdate')
	
	listTable=Task.query.all()
	return render_template('admin/atividades.html', form=form, listTable=listTable)

@admin.route('/admin/atividUpdate', methods=['GET', 'POST'])
def atividUpdate():
	print('Fazer update')
	form = AtividadeForm()
	print(request.args.get('update'))
	if request.method == 'POST' and form.salvar.id == "salvar":
		atividade = Task.query.filter_by(codTask=form.idAtividade.data).first_or_404()
		if atividade:
			atividade.idAtividade = form.idAtividade.data
			atividade.descricao = form.descricao.data
			try:
				db.session.commit()
				flash('Registro alterado com sucesso', 'info')
			except:
				db.session.rollback()
				flash('Registro falhou em alterar', 'danger')

	listTable=Task.query.all()
	return render_template('admin/atividades.html', form=form, listTable=listTable)