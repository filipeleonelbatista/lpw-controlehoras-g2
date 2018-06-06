from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required
from .formsClient import ClientsForm
from . import admin
from app.models import Client
from app import db

@admin.route('/admin/clientes', methods=['GET', 'POST'])
@login_required
def clientes():
	form = ClientsForm()
	if request.method == 'POST' and form.salvar.data == True:
		try:
			print(form.cnpj.data)
			print(form.nome.data)
			client = Client(clientCNPJ=form.cnpj.data, nameEmpresa=form.nome.data)
			print(client.clientCNPJ)
			db.session.add(client)
			db.session.commit()
			flash('Registrado com sucesso', 'success')
		except:
			db.session.rollback()
			flash('Registro falhou na adição', 'danger')

	elif request.method == 'GET' and request.args.get('delete'):
		try:
			client = Client.query.filter_by(clientCNPJ=request.args.get('delete')).first_or_404()
			db.session.delete(client)
			db.session.commit()
			flash('Registro apagado com sucesso', 'danger')
		except:
			db.session.rollback()
			flash('Registro falhou em apagar', 'danger')

	elif request.method == 'GET' and request.args.get('update'):
		client = Client.query.filter_by(clientCNPJ=request.args.get('update')).first_or_404()
		form.cnpj.data = client.clientCNPJ
		form.nome.data = client.nameEmpresa
		return render_template('admin/editClinet.html',form=form, action='clientUpdate')
	
	listTable=Client.query.all()
	return render_template('admin/clientes.html', form=form, listTable=listTable)

@admin.route('/admin/clientUpdate', methods=['GET', 'POST'])
@login_required
def clientUpdate():
	form = ClientsForm()
	print(request.args.get('update'))
	if request.method == 'POST' and form.salvar.id == "salvar":
		client = Client.query.filter_by(clientCNPJ=form.cnpj.data).first_or_404()
		if client:
			client.cnpj = form.cnpj.data
			client.nameEmpresa = form.nome.data
			try:
				db.session.commit()
				flash('Registro alterado com sucesso', 'info')
			except:
				db.session.rollback()
				flash('Registro falhou em alterar', 'danger')

	listTable=Client.query.all()
	return render_template('admin/clientes.html', form=form, listTable=listTable)
