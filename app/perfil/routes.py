from flask import render_template, redirect, request, url_for, flash
from .forms import PerfilForm
from . import perfil

@perfil.route('/perfil', methods=['GET', 'POST'])
def perfil():
	form = PerfilForm()
	return render_template('perfil/perfil.html', form=form)
	