from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user
from . import lancamentos
from .formLancamentos import lancamentoForm
from app import db
from app.models import Task, Lancamento, Binding


@lancamentos.route('/lancamentos', methods=['GET', 'POST'])
@login_required
def lancamentos():
    form = lancamentoForm()
    form.selectProjeto.choices = [(project.project_id, project.project.nameProject) for project in
                                  Binding.query.filter_by(users_id=current_user.id).all()]
    form.selectAtividade.choices = [(task.codTask, task.descricao) for task in Task.getAllTask()]
    if request.method == 'POST' and form.gravar.data == True:
        try:
            if form.validacao(form):
                flash('Falta preenchar um campo!', 'danger')
            else:
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
        try:
            if request.args.get('delete') == '':
                flash('Falta a matricula!', 'danger')
            else:
                print(request.args.get('delete'))
                lancament = Lancamento.query.filter_by(id=request.args.get('delete')).first_or_404()
                db.session.delete(lancament)
                db.session.commit()
                flash('Registro apagado com sucesso', 'danger')
        except:
            db.session.rollback()
            flash('Registro falhou em apagar', 'danger')

    elif request.method == 'GET' and request.args.get('update'):
        if request.args.get('update') == '':
            flash('Falta a matricula!', 'danger')
        else:
            lancamento = Lancamento.query.filter_by(id=request.args.get('update')).first_or_404()
            form.selectProjeto.process_data(lancamento.project_id)
            form.selectAtividade.process_data(lancamento.task_id)
            form.dtInicio.data = lancamento.dtInic
            form.hrInicio.data = lancamento.hrInic
            form.dtFim.data = lancamento.dtFim
            form.hrFim.data = lancamento.hrFim
            form.descricao.data = lancamento.descricao
            return render_template('lancamentos/editLacmento.html', form=form, act='lUpdate')
    lListLan = Lancamento.query.all()
    return render_template('lancamentos/lancamentos.html', form=form, listTable=lListLan)


@lancamentos.route('/lancamentos/lUpdate', methods=['GET', 'POST'])
@login_required
def update():
    form = lancamentoForm()
    print(form.dtInicio.data)
    return redirect(url_for('.lancamentos'))
