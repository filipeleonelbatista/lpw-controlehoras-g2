from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, login_required, logout_user
from .forms import LoginForm
from . import auth
from ..models import User

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None or not user.verify_password(form.password.data):
            flash('Invalid name or password')
            return redirect(url_for('.login'))
        login_user(user, form.remember_me.data)
        return redirect(request.args.get('next') or url_for('dashaboard.dashaboard'))
    return render_template('auth/login.html', form=form)

@auth.route('/acesso_negado')
def acesso():
    return render_template('/acesso_negado.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(request.args.get('next') or url_for('auth.login'))
