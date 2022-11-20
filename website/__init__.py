from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['secret_key'] = 'hello123'

    with app.app_context():
    
        from .views import views
        from .views import auth
    
        app.register_blueprint(views, url_prefix='/')
        
    return app

