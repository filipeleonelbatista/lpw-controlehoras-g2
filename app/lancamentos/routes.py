from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required

from app.lancamentos.formLancamentos import lancamentoForm
from .formLancamentos import lancamentoForm
from . import lancamentos
from app import db
from app.models import Lancamento, Task, Project

@lancamentos.route('/lancamentos', methods=['GET', 'POST'])
@login_required
def lancamento():
    print('Preparando para registrar, deletar, alterar')

    form = lancamentoForm()
    form.selectProjeto.choices = [(project.id, project.nameProject) for project in Project.getAllProject()]
    form.selectAtividade.choices = [(task.codTask, task.descricao) for task in Task.getAllTask()]

    if request.method == 'POST' and form.gravar.data == True:
        print('cadastro')
        if form.validacao(form):
            flash('Falta preenchar um campo!', 'danger')
        else:
            try:
                lancam = Lancamento(project_id=form.selectProjeto.data, dtInic=form.dtInicio.data,
                                    hrInic=form.hrInicio.data,
                                    dtFim=form.dtFim.data, hrFim=form.hrFim.data, task_id=form.selectAtividade.data,
                                    descricao=form.descricao.data)
                db.session.add(lancam)
                db.session.commit()
                flash('Registrado com sucesso', 'success')
            except:
                db.session.rollback()
                flash('Registro falhou na adição', 'danger')
    elif request.method == 'GET' and request.args.get('delete'):
        print('Apagando registro')
        if request.args.get('delete') == '':
            print('erro ao apagar')
            flash('Falta a identificacao da tabela!', 'danger')
        else:
            print('preparando para apgar o registro')
            print(request.args.get('delete'))
            try:
                lancament = Lancamento.query.filter_by(id=request.args.get('delete')).first_or_404()
                db.session.delete(lancament)
                db.session.commit()
                flash('Registro apagado com sucesso', 'danger')
            except:
                db.session.rollback()
                flash('Registro falhou em apagar', 'danger')
    elif request.method == 'GET' and request.args.get('update'):
        print('Alteracao de regsitro')
        if request.args.get('update') == '':
            flash('Falta a matricula!', 'danger')
        else:
            print('Faendo alteracao do registro')
            IDLancUpdate = request.args.get('update')
            lancamento = Lancamento.query.filter_by(id=IDLancUpdate).first_or_404()
            form.selectProjeto.process_data(lancamento.project_id)
            form.selectAtividade.process_data(lancamento.task_id)
            form.dtInicio.data = lancamento.dtInic
            form.hrInicio.data = lancamento.hrInic
            form.dtFim.data = lancamento.dtFim
            form.hrFim.data = lancamento.hrFim
            form.descricao.data = lancamento.descricao
            form.idLac.data = lancamento.id
            return render_template('lancamentos/editLacmento.html', form=form, action='lUpdate')

    #mantem a lista altualizada
    lListTable=Lancamento.query.all()
    return render_template('lancamentos/lancamentos.html', form=form, listTable=lListTable)

@lancamentos.route('/lUpdate', methods=['GET', 'POST'])
@login_required
def lUpdate():
    print('Preparando para fazer alteracao')
    form = lancamentoForm(request.form)  # type: lancamentoForm
    if request.method == 'POST' and form.salvar.data == True:
        if form.validacao(form):
            flash('Falta preenchar um campo!', 'danger')
        else:
            print('Fazendo a alteração propriamente dito')
            print(form.idLac.data)
            print(request.form)
            lancamento = Lancamento.query.filter_by(id=form.idLac.data).first_or_404()
            if lancamento:
                lancamento.project_id = form.selectProjeto.data
                lancamento.dtInic = form.dtInicio.data
                lancamento.hrInic = form.hrInicio.data
                lancamento.dtFim = form.dtFim.data
                lancamento.hrFim = form.hrFim.data
                lancamento.task_id = form.selectAtividade.data
                lancamento.descricao = form.descricao.data
                try:
                    db.session.commit()
                    flash('Registro alterado com sucesso', 'info')
                except:
                    db.session.rollback()
                    flash('Registro falhou em alterar', 'danger')
                    
    form.selectProjeto.choices = [(project.id, project.nameProject) for project in Project.getAllProject()]
    form.selectAtividade.choices = [(task.codTask, task.descricao) for task in Task.getAllTask()]
    # mantem a lista altualizada
    lListTable = Lancamento.query.all()
    return render_template('lancamentos/lancamentos.html', form=form, listTable=lListTable)