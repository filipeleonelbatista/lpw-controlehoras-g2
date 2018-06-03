from flask import render_template, redirect, request, url_for, flash
from flask_table import Table
from .formsVinculacao import VincForm
from . import admin
from app import db
from app.models import User, Project, Binding

@admin.route('/admin/vinculacao', methods=['GET', 'POST'])
def vinculacao():
	form = VincForm()
	form.selectFunc.choices = [(user.id, user.username) for user in User.getAllUsers()]
	form.selectProj.choices = [(project.id, project.nameProject) for project in Project.getAllProject()]

	if request.method == 'POST' and form.salvar.id == "salvar":
		try:			
			binding = Binding(
				idBinding=form.codVinc.data, 
				project_id=form.selectProj.data,
				users_id=form.selectFunc.data,
				is_coord=form.coordenador.data
				)
			db.session.add(binding)
			db.session.commit()
			flash('Registrado com sucesso', 'success')
		except:
			db.session.rollback()
			flash('Registro falhou na adição', 'danger')

	elif request.method == 'GET' and request.args.get('delete'):
		try:
			binding = Binding.query.filter_by(idBinding=request.args.get('delete')).first_or_404()
			db.session.delete(binding)
			db.session.commit()
			flash('Registro apagado com sucesso', 'danger')
		except:
			db.session.rollback()
			flash('Registro falhou em apagar', 'danger')

	# elif request.method == 'GET' and request.args.get('update'):
	# 	binding = Binding.query.filter_by(idBinding=request.args.get('update')).first_or_404()
	# 	form.codProj.data = binding.idBinding
	# 	form.nomeProj.data = binding.nameProject	
	# 	#form.selectClient.choices = [(client.id, client.nameEmpresa) for client in Client.getAllClient()]
	# 	client=Client.getClientID(binding.client_id)
	# 	form.selectClient.choices = [(client.id, client.nameEmpresa)]
	# 	form.descrProj.data = binding.descricao
	# 	return render_template('admin/editProject.html',form=form, action='projectUpdate')
	
	listTable=Binding.query.all()
	return render_template('admin/vinculacao.html', form=form, listTable=listTable)
