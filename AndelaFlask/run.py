from flask import Flask
from config import DevelopmentConfig


def create_app():

    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from models import db
    db.init_app(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
