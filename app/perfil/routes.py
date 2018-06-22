from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user
from .forms import PerfilForm
from . import perfil

@perfil.route('/perfil', methods=['GET', 'POST'])
@login_required
def perfil():
	form = PerfilForm()
	return render_template('perfil/perfil.html', form=form)
	