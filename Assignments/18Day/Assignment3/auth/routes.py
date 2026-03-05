from flask import Blueprint, request, jsonify, session

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json

    username = data.get("username")

    if not username:
        return jsonify({"error": "Username required"}), 400

    session["username"] = username

    return jsonify({
        "message": "Login successful",
        "user": username
    })