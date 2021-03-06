from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user
from .formsVinculacao import VincForm
from . import admin
from app import db
from app.models import User, Project, Binding


@admin.route('/admin/vinculacao', methods=['GET', 'POST'])
@login_required
def vinculacao():
    if not current_user.is_admin:
        return redirect(url_for('auth.acesso'))

    form = VincForm()
    form.selectFunc.choices = [(user.id, user.username) for user in User.getAllUsers()]
    form.selectProj.choices = [(project.id, project.nameProject) for project in Project.getAllProject()]

    if request.method == 'POST' and form.salvar.data == True:
        try:
            last = Binding.query.all()
            if last:
                idBindingProx = (last[-1].idBinding + 1)
            else:
                idBindingProx = 1

            if form.validInteger(idBindingProx):
                flash('ID da vinculacao deve ser composto de somente numeros!', 'danger')
            else:
                binding = Binding(
                    idBinding=idBindingProx,
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
            if request.args.get('delete') == '':
                flash('Falta o ID da vinculacao!', 'danger')
            else:
                binding = Binding.query.filter_by(idBinding=request.args.get('delete')).first_or_404()
                db.session.delete(binding)
                db.session.commit()
                flash('Registro apagado com sucesso', 'info')
        except:
            db.session.rollback()
            flash('Registro falhou em apagar', 'danger')

    elif request.method == 'GET' and request.args.get('update'):
        if request.args.get('update') == '':
            flash('Falta o ID da vinculacao!', 'danger')
        else:
            binding = Binding.query.filter_by(idBinding=request.args.get('update')).first_or_404()
            form.codVinc.data = binding.idBinding
            form.selectProj.choices = [(project.id, project.nameProject) for project in Project.getAllProject()]
            form.selectProj.process_data(binding.project_id)
            form.selectFunc.choices = [(user.id, user.username) for user in User.getAllUsers()]
            form.selectFunc.process_data(binding.users_id)
            form.coordenador.data = binding.is_coord
            return render_template('admin/editVinculacao.html', form=form, action='vinctUpdate')

    listTable = Binding.query.all()
    return render_template('admin/vinculacao.html', form=form, listTable=listTable)


@admin.route('/admin/vinctUpdate', methods=['GET', 'POST'])
@login_required
def vinctUpdate():
    if not current_user.is_admin:
        flash('Solicite o auxilio do adminstrador do sistema!', 'danger')
        return redirect(url_for('dashaboard.dashaboard'))

    form = VincForm()
    if request.method == 'POST' and form.salvar.data == True:
        if form.validInteger(int(form.codVinc.data)):
            flash('ID da vinculacao deve ser composto de somente numeros!', 'danger')
        else:
            binding = Binding.query.filter_by(idBinding=form.codVinc.data).first_or_404()
            if binding:
                binding.idBinding = form.codVinc.data
                binding.project_id = form.selectProj.data
                binding.users_id = form.selectFunc.data
                binding.is_coord = form.coordenador.data
                try:
                    db.session.commit()
                    flash('Registro alterado com sucesso', 'info')
                except:
                    db.session.rollback()
                    flash('Registro falhou em alterar', 'danger')
    return redirect(url_for('.vinculacao'))
