from flask import Blueprint, jsonify, request, abort
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import datetime

from main import db, bcrypt
from models.user import User
from schemas.User_Schema import UserSchema
from custom_decorator import admin_required




# auth blueprint
home = Blueprint("auth", __name__, url_prefix="/home")


#register and create user
@home.route("/register", methods=["POST"])
def register_user():
    user_json = request.json

    # Deserialize and validate user data using User_Schema
    errors = UserSchema().validate(user_json)

    if errors:
        return jsonify(errors), 400

    # Check if the email is already in use
    existing_user = User.query.filter_by(email=user_json["email"]).first()
    if existing_user:
        return jsonify({"message": "email already in use"}), 400

    # Hash the user's password before storing it in the database
    password_hash = bcrypt.generate_password_hash(user_json["password"]).decode("utf-8")

    # Create a new User object and add it to the database
    new_user = User(
        username=user_json["username"],
        email=user_json["email"],
        password=password_hash,
        registration_date=datetime.utcnow()  
    )

    db.session.add(new_user)
    db.session.commit()

    # Create an access token for the new user
    access_token = create_access_token(identity=new_user.user_id)
    return jsonify({"token": access_token}), 201



#logging in a user
@home.route("/login", methods=["POST"])
@jwt_required()
def login_user():
    user_json = request.json
    email = user_json.get("email")
    password = user_json.get("password")

    # Find the user by email in the database
    user = User.query.filter_by(email=email).first()

    #When input information is wrong
    if not user or not bcrypt.check_password_hash(user.password, password):
        return abort(401, description="Invalid credentials")

    # Create an access token for the authenticated user
    access_token = create_access_token(identity=user.user_id)
    return jsonify({"token": access_token}), 200



#route to delete self
@home.route('/user_delete/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    user = User.query.get(user_id)
    
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": f"User {user_id} deleted successfully"})
    else:
        return jsonify({"message": "User not found"}), 404


# Route to delete a user by user_id, only accessible to administrators
@home.route('/admin_delete/<int:user_id>', methods=['DELETE'])
@jwt_required()
@admin_required()  
def delete_user_as_admin(user_id):
    user = User.query.get(user_id)
    
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": f"Admin deleted user {user_id} successfully"})
    else:
        return jsonify({"message": "User not found"}), 404