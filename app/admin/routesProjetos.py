from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required
from .formsProjetos import ProjetoForm
from . import admin
from app import db
from app.models import Client, Project

@admin.route('/admin/projetos', methods=['GET', 'POST'])
@login_required
def projetos():	
	form = ProjetoForm()
	form.selectClient.choices = [(client.id, client.nameEmpresa) for client in Client.getAllClient()]
	
	if request.method == 'POST' and form.salvar.id == "salvar":
		try:			
			project = Project(
				codProject=form.codProj.data, 
				nameProject=form.nomeProj.data,
				client_id=form.selectClient.data,
				descricao=form.descrProj.data
				)
			db.session.add(project)
			db.session.commit()
			flash('Registrado com sucesso', 'success')
		except:
			db.session.rollback()
			flash('Registro falhou na adição', 'danger')

	elif request.method == 'GET' and request.args.get('delete'):
		try:
			project = Project.query.filter_by(codProject=request.args.get('delete')).first_or_404()
			db.session.delete(project)
			db.session.commit()
			flash('Registro apagado com sucesso', 'danger')
		except:
			db.session.rollback()
			flash('Registro falhou em apagar', 'danger')

	elif request.method == 'GET' and request.args.get('update'):
		project = Project.query.filter_by(codProject=request.args.get('update')).first_or_404()
		form.codProj.data = project.codProject
		form.nomeProj.data = project.nameProject	
		form.selectClient.choices = [(client.id, client.nameEmpresa) for client in Client.getAllClient()]
		form.selectClient.process_data(project.client_id)
		form.descrProj.data = project.descricao
		return render_template('admin/editProject.html',form=form, action='projectUpdate')
	
	listTable=Project.query.all()
	return render_template('admin/projetos.html', form=form, listTable=listTable)

@admin.route('/admin/projectUpdate', methods=['GET', 'POST'])
@login_required
def projectUpdate():
	form = ProjetoForm()
	print(request.args.get('update'))
	if request.method == 'POST' and form.salvar.id == "salvar":
		project = Project.query.filter_by(codProject=form.codProj.data).first_or_404()
		if project:
			project.codProject = form.codProj.data
			project.nameProject = form.nomeProj.data
			project.client_id = form.selectClient.data
			project.descricao = form.descrProj.data
			try:
				db.session.commit()
				flash('Registro alterado com sucesso', 'info')
			except:
				db.session.rollback()
				flash('Registro falhou em alterar', 'danger')

	listTable=Project.query.all()
	return render_template('admin/projetos.html', form=form, listTable=listTable)