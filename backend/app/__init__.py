from flask import Flask
from app.config import Config
from app.models import db
from app.routes import api_blueprint
from flask_cors import CORS

def create_app():
    print("CORS is enabled")
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Register Blueprints first
    app.register_blueprint(api_blueprint)

    # Then enable CORS globally
    from flask_cors import CORS
    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)


    # You can restrict to specific origins if needed

    return app
