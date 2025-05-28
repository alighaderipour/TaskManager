from flask import Blueprint, jsonify
from app.models import Task

tasks_bp = Blueprint('tasks', __name__, url_prefix='/api/tasks')

@tasks_bp.route('/<int:user_id>', methods=['GET'])
def get_tasks(user_id):
    tasks = Task.query.filter_by(user_id=user_id).all()
    return jsonify([{
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "is_completed": task.is_completed
    } for task in tasks])
