from flask import Blueprint
from app.routes.auth_routes import auth_bp
from app.routes.tasks_routes import tasks_bp

api_blueprint = Blueprint('api', __name__)

# Register sub-blueprints
api_blueprint.register_blueprint(auth_bp)
api_blueprint.register_blueprint(tasks_bp)
