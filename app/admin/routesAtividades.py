from flask import render_template, redirect, request, url_for, flash
from sqlalchemy import inspect
from flask_login import login_required, current_user
from .formsAtividades import AtividadeForm
from . import admin
from app.models import Task
from app import db


@admin.route('/admin/atividades', methods=['GET', 'POST'])
@login_required
def atividades():
    if not current_user.is_admin:
        return redirect(url_for('auth.acesso'))

    form = AtividadeForm()
    if request.method == 'POST' and form.salvar.data == True:
        try:
            last = Task.query.all()
            if last:
                idTaskProx = (last[-1].codTask + 1)
            else:
                idTaskProx = 1
                
            if form.validacao(form):
                flash('Falta preenchar um campo!', 'danger')
            elif form.validInteger(idTaskProx):
                flash('ID da atividade deve ser composto de somente numeros!', 'danger')
            else:
                atividade = Task(codTask=idTaskProx, descricao=form.descricao.data)
                db.session.add(atividade)
                db.session.commit()
                flash('Registrado com sucesso', 'success')
        except:
            db.session.rollback()
            flash('Registro falhou na adição', 'danger')

    elif request.method == 'GET' and request.args.get('delete'):
        try:
            if request.args.get('delete') == '':
                flash('Falta a atividade!', 'danger')
            else:
                atividade = Task.query.filter_by(codTask=request.args.get('delete')).first_or_404()
                db.session.delete(atividade)
                db.session.commit()
                flash('Registro apagado com sucesso', 'info')
        except:
            db.session.rollback()
            flash('Registro falhou em apagar', 'danger')

    elif request.method == 'GET' and request.args.get('update'):
        if request.args.get('update') == '':
            flash('Falta a atividade!', 'danger')
        else:
            atividade = Task.query.filter_by(codTask=request.args.get('update')).first_or_404()
            form.idAtividade.data = atividade.codTask
            form.descricao.data = atividade.descricao
            return render_template('admin/editAtividade.html', form=form, action='atividUpdate')

    listTable = Task.query.all()
    return render_template('admin/atividades.html', form=form, listTable=listTable)


@admin.route('/admin/atividUpdate', methods=['GET', 'POST'])
@login_required
def atividUpdate():
    if not current_user.is_admin:
        flash('Solicite o auxilio do adminstrador do sistema!', 'danger')
        return redirect(url_for('dashaboard.dashaboard'))

    print('Fazer update')
    form = AtividadeForm()
    if request.method == 'POST' and form.salvar.data == True:
        if form.validacao(form):
            flash('Falta preenchar um campo!', 'danger')
        elif form.validInteger(int(form.idAtividade.data)):
            flash('ID da atividade deve ser composto de somente numeros!', 'danger')
        else:
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
    return redirect(url_for('.atividades'))
