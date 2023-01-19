from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'test'
    
    # register blueprints
    from core.main import bp as main_bp
    app.register_blueprint(main_bp)

    @app.route('/test/')
    def test():
        return 'test successful'

    return app