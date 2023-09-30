from flask import Blueprint
from main import db
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from schemas import UserLibrarySchema, User_Schema
from models import User_Library, User, Game


# Create a blueprint for user library routes
library = Blueprint("library", __name__, url_prefix="/library")


#route to list all libraries
@library.route("/all")
def list_all_libraries():
    try:
        # Query the database to retrieve all user library entries
        all_user_libraries = User_Library.query.all()

        # Create a list to store all library entries with nested game information
        all_library_entries = []

        for library in all_user_libraries:
            # Retrieve game information for each library entry
            game = Game.query.get(library.game_id)

            if game:
                # Serialize the library entry and nested game info
                library_data = {
                    "user_library_id": library.user_library_id,
                    "user_id": library.user_id,
                    "username": User.username,
                    "game_id": library.game_id,
                    "game": {
                        "game_id": game.game_id,
                        "title": game.title,
                        "description": game.description,
                    }
                }

                all_library_entries.append(library_data)

        # Return the list of all library entries with nested game information as JSON
        return jsonify(all_library_entries), 200

    except Exception as e:
        # Handle exceptions and return an error response if needed
        return jsonify({"message": "An error occurred"}), 500
    


#route to view a users library by user_id
@library.route("/library/user/<int:user_id>", methods=["GET"])
def get_user_library_entries(user_id):
    try:
        # Query the database to retrieve all library entries for the specified user_id
        library_entries = User_Library.query.filter_by(user_id=user_id).all()

        # Serialize the list of library entries using UserLibrarySchema (create this schema)
        user_library_schema = UserLibrarySchema(many=True)
        library_data = user_library_schema.dump(library_entries)

        # Return the list of library entries as JSON
        return jsonify(library_data), 200

    except Exception as e:
        # Handle exceptions and return an error response if needed
        return jsonify({"message": "An error occurred"}), 500