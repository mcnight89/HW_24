from flask import Flask
from HW_23.views import main_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(main_bp)
    return app
