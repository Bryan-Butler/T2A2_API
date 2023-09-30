from flask import Blueprint, jsonify, request, abort
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import datetime

from main import db, bcrypt
from models import User, User_Library
from schemas import UserSchema
from .custom_decorator import admin_required




# home blueprint
home = Blueprint("home", __name__, url_prefix="/")




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
        return jsonify({"message": "Email already in use"}), 400

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

    # When input information is wrong
    if not user or not bcrypt.check_password_hash(user.password, password):
        return jsonify({"message": "Invalid credentials"}), 401

    # Create an access token for the authenticated user
    access_token = create_access_token(identity=user.user_id)
    return jsonify({"token": access_token}), 200




#get user by user_id
@home.route("/user/<int:user_id>", methods=["GET"])
@jwt_required()
def get_user_profile(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({"message": "User not found"}), 404


    user_data = {
        "user_id": user.user_id,
        "username": user.username,
    }

    return jsonify(user_data), 200




#show a users library by user_id
@home.route("/user/<int:user_id>/library")
@jwt_required()
def get_user_library(user_id):
    # Query the database to retrieve the user's library by their user_id
    user_library = User_Library.query.filter_by(user_id=user_id).all()

    if not user_library:
        return jsonify({"message": "User's library not found"}), 404

    library_data = []

    for item in user_library:
        library_item = {
            "game_id": item.game_id,
            "game_title": item.game.title,
            "added_date": item.added_date,
        }
        library_data.append(library_item)

    return jsonify(library_data), 200




# Route to update user profile by user_id
@home.route("/update_user/<int:user_id>", methods=["PUT"])
@jwt_required()
def update_user_profile(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({"message": "User not found"}), 404

    current_user_id = get_jwt_identity()

    # Check if the user is trying to update their own profile
    if current_user_id != user_id:
        return jsonify({"message": "Permission denied. You can only update your own profile"}), 403

    user_json = request.json

    # Initialize UserSchema for validation
    user_schema = UserSchema()

    # Validate the user data
    errors = user_schema.validate(user_json)

    if errors:
        return jsonify(errors), 400

    # Update user profile fields based on the incoming data
    # Update username
    if "username" in user_json:
        user.username = user_json["username"]

    # Update email
    if "email" in user_json:
        user.email = user_json["email"]

    # Update password 
    if "password" in user_json:
        password_hash = bcrypt.generate_password_hash(user_json["password"]).decode("utf-8")
        user.password = password_hash

    # Commit the changes to the database
    db.session.commit()

    return jsonify({"message": "User profile updated successfully"}), 200



#route to show ALL users
@home.route("/users", methods=["GET"])
@jwt_required()
@admin_required
def get_all_users():
    # Query the database to retrieve all users
    users = User.query.all()

    # Serialize the list of users
    user_schema = UserSchema(many=True)
    users_data = user_schema.dump(users)

    return jsonify(users_data), 200