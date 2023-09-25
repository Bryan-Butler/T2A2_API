from flask import Blueprint, jsonify, request, abort
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from main import db, bcrypt
from models.user import User
from schemas import User_Schema


# auth blueprint
auths = Blueprint("auth", __name__, url_prefix="/auth")

#register and create user
@auths.route("/register", methods=["POST"])
def register_user():
    user_json = User_Schema.load(request.json)
    user = User(
        {
            "email": user_json["email"],
            "admin": False,
            "password": bcrypt.generate_password_hash(user_json["password"]).decode("utf")
        }
    )
    db.session.add(user)
    db.session.commit()

    access_token = create_access_token(identity=user_json["email"])

    return jsonify({"token": access_token})


#logging a user in
@auths.route("/login", methods=['POST'])
@jwt_required
def login_user():
    email = request.json["email"]
    password = request.json["password"]

    q = db.select(user).filter_by(email=email)
    user = db.session.scalar(q)

    if not user or not bcrypt.check_password_hash(user.password, password):
        return abort(401, description="")
    
    return jsonify({"message": "success", **User_Schema.dump(user)})


#if a user is already logged in
@auths.route("/already-logged-in", methods=["POST"])
@jwt_required()
def already_logged_in():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200