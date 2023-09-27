from main import db
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from models import User
from authorize_helpers import admin_required


delete = Blueprint("delete",__name__, url_prefix="/delete")

#route to delete self
@delete.route('/user_delete/<int:User_ID>', methods=['DELETE'])
@jwt_required()
def delete_user(User_ID):
    current_user_id = get_jwt_identity()
    if current_user_id == User_ID:
        user = User.query.get(User_ID)
        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify({"message": f"User {User_ID} deleted successfully"})
        else:
            return jsonify({"message": "User not found"}), 404
    else:
        return jsonify({"message": "Permission denied. You can only delete your own account"}), 403

# Route to delete a user by User_ID, only accessible to administrators
@delete.route('/admin/delete/<int:User_ID>', methods=['DELETE'])
@jwt_required()
@admin_required()
def delete_user_as_admin(User_ID):
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)
    if current_user and current_user.Is_Admin:
        user = User.query.get(User_ID)
        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify({"message": f"Admin deleted user {User_ID} successfully"})
        else:
            return jsonify({"message": "User not found"}), 404
    else:
        return jsonify({"message": "Permission denied. User is not an admin"}), 403
