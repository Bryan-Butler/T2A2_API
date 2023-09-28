from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from main import db
from models import User


#function to check for admin privileges
def admin_required(func):
    def decorated_function():
        current_user_id = get_jwt_identity()

        #check user exists
        if current_user_id is None:
            return jsonify(message="User not authenticated"), 401

        user = db.session.query(User).filter_by(user_id=current_user_id).first()

        #when user doesnt exist
        if not user:
            return jsonify(message="User not found"), 404

        #if user is not an admin
        if not user.is_admin:
            return jsonify(message="Admin privileges required"), 403

        return func()

    return decorated_function