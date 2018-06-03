import hashlib
from datetime import datetime

from flask import request

from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(UserMixin, db.Model, Base):
    print('Preparando para adicionar o funcionarios')
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False, index=True)
    matricula = db.Column(db.Integer, nullable=False, unique=True, index=True)
    is_admin = db.Column(db.Boolean)
    password_hash = db.Column(db.String(256))
    binding = relationship("Binding")
    #avatar_hash = db.Column(db.String(256))
    #talks = db.relationship('Talk', lazy='dynamic', backref='author')

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def gravatar(self, size=100, default='identicon', rating='g'):
        if request.is_secure:
            url = 'https://secure.gravatar.com/avatar'
        else:
            url = 'http://www.gravatar.com/avatar'
        hash = self.avatar_hash or hashlib.md5(self.email.encode('utf-8')).hexdigest()
        return "{url}/{hash}?s={size}&d={default}&r={rating}".format(url=url, hash=hash, size=size, default=default, rating=rating)

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
    nameProject = db.Column(db.String(64), nullable=False, unique=True, index=True)
    client_id = db.Column (db.Integer, db.ForeignKey('client.id'),
        nullable = False)
    descricao = db.Column(db.String(64))
    binding = relationship("Binding")

class Binding(UserMixin, db.Model, Base):
    print('Preparando para adicionar o binding')
    __tablename__ = 'binding'
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class Task(UserMixin, db.Model):
    print('Preparando para adicionar o task')
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    codTask = db.Column(db.Integer, nullable=False, unique=True, index=True)
    descricao = db.Column(db.String(64))
