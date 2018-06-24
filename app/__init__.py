from flask import Flask
from config import config
from flask_bootstrap import Bootstrap
from flask_datepicker import datepicker
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_gravatar import Gravatar

gravatar = Gravatar()

bootstrap = Bootstrap
Datepicker = datepicker
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .perfil import perfil as perfil_blueprint
    app.register_blueprint(perfil_blueprint)

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)

    from .relatorios import relatorios as relatorios_blueprint
    app.register_blueprint(relatorios_blueprint)

    from .lancamentos import lancamentos as lancamentos_blueprint
    app.register_blueprint(lancamentos_blueprint)

    # Inicializando app Bootstrap
    bootstrap(app)
    # Inicializando app datepiker
    Datepicker(app)

    # Inicializando Database
    db.init_app(app)

    gravatar.init_app(app)

    # Inicializando Autenticacao
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    login_manager.init_app(app)

    return app
