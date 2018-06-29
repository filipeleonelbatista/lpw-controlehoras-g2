from flask import render_template, redirect, request, url_for, flash
from .forms import HomeForm
from . import home

@home.route('/home', methods=['GET', 'POST'])
def home():
	form = HomeForm()
	return render_template('home/home.html', form=form)