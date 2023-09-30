from flask import Blueprint, request, jsonify
from main import db
from flask_jwt_extended import jwt_required


from models import Genre
from .custom_decorator import admin_required

genre = Blueprint("genre", __name__, url_prefix='/genres')


#route to get all genres
@genre.route("/", methods=["GET"])
def get_all_genres():
    genres = Genre.query.all()
    genre_list = [{"genre_id": genre.genre_id, "genre_name": genre.genre_name} for genre in genres]
    return jsonify({"genres": genre_list})



#route to get genre by id
@genre.route("/<int:genre_id>", methods=["GET"])
def get_genre_by_id(genre_id):
    genre = Genre.query.get_or_404(genre_id)
    return jsonify({"genre_id": genre.genre_id, "genre_name": genre.genre_name})


#route to update genre by id
@genre.route("/update/<int:genre_id>", methods=["PUT", "PATCH"])
@jwt_required()  
@admin_required
def update_genre(genre_id):
    genre = Genre.query.get_or_404(genre_id)
    data = request.get_json()
    
    # Update the genre_name directly
    genre.genre_name = data['genre_name']
    
    db.session.commit()
    return jsonify({"message": "Genre updated successfully"})


#route to create a new genre, admin only
@genre.route("/create", methods=["POST"])
@jwt_required()
@admin_required 
def create_genre():
    data = request.get_json()
    
    # Create a new genre
    new_genre = Genre(genre_name=data['genre_name'])
    db.session.add(new_genre)
    db.session.commit()
    
    return jsonify({"message": "Genre created successfully"}), 201



#route to delete by genre id, admin only
@genre.route("/delete/<int:genre_id>", methods=["DELETE"])
@jwt_required()
@admin_required
def delete_genre(genre_id):
    genre = Genre.query.get_or_404(genre_id)
    db.session.delete(genre)
    db.session.commit()
    return jsonify({"message": "Genre deleted successfully"})