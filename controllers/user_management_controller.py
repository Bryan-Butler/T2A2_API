from flask import Blueprint, jsonify, request, abort
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import datetime

from main import db
from models.user import User
from schemas.User_Schema import UserSchema
from .custom_decorator import admin_required





# user management blueprint
user_management = Blueprint("user_management", __name__, url_prefix="/management")

@user_management.route('/user_delete/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    user = User.query.get(user_id)

    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": f"User {user_id} deleted successfully"}), 200
    else:
        return jsonify({"message": "User not found"}), 404
    

@user_management.route('/admin_delete/<int:user_id>', methods=['DELETE'])
@jwt_required()
@admin_required
def delete_user_as_admin(user_id):
    user = User.query.get(user_id)

    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": f"Admin deleted user {user_id} successfully"}), 200
    else:
        return jsonify({"message": "User not found"}), 404