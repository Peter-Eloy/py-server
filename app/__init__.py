from flask import Flask
from .config import Config
from .routes.main import main_bp
from .routes.admin import admin_bp
from .routes.api import api_bp
from .models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
    
    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(api_bp, url_prefix='/api')
    
    return app