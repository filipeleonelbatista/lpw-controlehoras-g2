import hashlib
from datetime import datetime

from flask import request

from . import db, login_manager, gravatar
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from flask_gravatar import Gravatar

Base = declarative_base()

class User(UserMixin, db.Model, Base):
    print('Preparando para adicionar o funcionarios')
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    fullusername = db.Column(db.String(64), nullable=False, index=True)
    username = db.Column(db.String(64), nullable=False, index=True)
    matricula = db.Column(db.Integer, nullable=False, unique=True, index=True)
    is_admin = db.Column(db.Boolean)
    email = db.Column(db.String(64), nullable=False, unique=True, index=True)
    avatar_hash = db.Column(db.String(256))
    password_hash = db.Column(db.String(256))
    binding = db.relationship( 'Binding', backref = 'users', lazy = True)
    lancamento = db.relationship('Lancamento', backref='users', lazy=True)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def gravatar(self, size=100, default='identicon', rating='g'):
        return gravatar(self.email, size, rating)
        # if request.is_secure:
        #     url = 'https://secure.gravatar.com/avatar'
        # else:
        #     url = 'http://www.gravatar.com/avatar'
        # hash = self.avatar_hash or hashlib.md5(self.email.encode('utf-8')).hexdigest()
        # return "{url}/{hash}?s={size}&d={default}&r={rating}".format(url=url, hash=hash, size=size, default=default, rating=rating)

    def getAllUsers():
        return User.query.all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Client(UserMixin, db.Model):
    print('Preparando para adicionar o cliente')
    __tablename__ = 'client'
    id = db.Column(db.Integer, primary_key=True)
    nameEmpresa = db.Column(db.String(64), nullable=False, index=True)
    clientCNPJ = db.Column(db.String(64), nullable=False, unique=True, index=True)
    project = db.relationship( 'Project', backref = 'client', lazy = True)
    
    def getAllClient():
        return Client.query.all()

    def getClientID(client_id):
        return Client.query.get(int(client_id))
    
class Project(UserMixin, db.Model, Base):
    print('Preparando para adicionar o project')
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True)
    codProject = db.Column(db.Integer,nullable=False, unique=True, index=True)
    nameProject = db.Column(db.String(64), nullable=False, index=True)
    client_id = db.Column (db.Integer, db.ForeignKey('client.id'),
        nullable = False)
    descricao = db.Column(db.String(64))
    binding = db.relationship( 'Binding', backref = 'project', lazy = True)
    lancamento = db.relationship( 'Lancamento', backref = 'project', lazy = True)

    def getAllProject():
        return Project.query.all()

    def getProjectID(idProject):
        return Project.query.filter_by(codProject=idProject)

class Binding(UserMixin, db.Model, Base):
    print('Preparando para adicionar o binding')
    __tablename__ = 'binding'
    id = db.Column(db.Integer, primary_key=True)
    idBinding = db.Column(db.Integer, nullable=False, unique=True, index=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    is_coord = db.Column(db.Boolean)

    def getBinding_UserID(idUser):
        return Binding.query.filter_by(users_id=idUser)

class Lancamento(UserMixin, db.Model):
    print('Preparando para adicionar o lancamentos')
    __tablename__ = 'lancamentos'
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'))
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    dtInic = db.Column(db.Date)
    hrInic = db.Column(db.Time)
    dtFim = db.Column(db.Date)
    hrFim = db.Column(db.Time)
    descricao = db.Column(db.String(256))

    def getAllLancamento():
        return Lancamento.query.all()

class Task(UserMixin, db.Model):
    print('Preparando para adicionar o task')
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    codTask = db.Column(db.Integer, nullable=False, unique=True, index=True)
    descricao = db.Column(db.String(64))
    lancamento = db.relationship( 'Lancamento', backref = 'task', lazy = True)

    def getAllTask():
        return Task.query.all()
