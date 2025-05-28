from flask import Blueprint, request, jsonify
from app.models import db, User  # And any other models you need

auth_bp = Blueprint('auth', __name__, url_prefix='/')


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        return jsonify({"message": "Login successful", "user_id": user.id})
    return jsonify({"message": "Invalid credentials"}), 401




@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Missing username or password"}), 400

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({"message": "Username already exists"}), 409

    new_user = User(username=username)
    new_user.set_password(password)  # Use secure password storage
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201