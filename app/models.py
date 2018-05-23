import hashlib
from datetime import datetime

from flask import request

from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    print('Preparando para adicionar o funcionarios')
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False, unique=True, index=True)
    matricula = db.Column(db.Integer, nullable=False, unique=True, index=True)
    is_admin = db.Column(db.Boolean)
    password_hash = db.Column(db.String(256))
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
    __tablename__ = 'client'
    id = db.Column(db.Integer, primary_key=True)    
    nameEmpresa = db.Column(db.String(64), nullable=False, unique=True, index=True)
    clientCNPJ = db.Column(db.String(64), nullable=False, unique=True, index=True)
    
class Project(UserMixin, db.Model):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True)
    codProject = db.Column(db.Integer)
    nameProject = db.Column(db.String(64), nullable=False, unique=True, index=True)
    #colocar o id do cliente aqui
    descricao = db.Column(db.String(64))
    
class Binding(UserMixin, db.Model):
    __tablename__ = 'binding'
    id = db.Column(db.Integer, primary_key=True)
    codBinding = db.Column(db.Integer)
    #colocar o id do funcionario aqui
    #colocar o id do projeto aqui
    is_coord = db.Column(db.Boolean)

class Task(UserMixin, db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    codTask = db.Column(db.Integer)
    descricao = db.Column(db.String(64))
