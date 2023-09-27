from flask import Blueprint, jsonify
from main import db
from flask_jwt_extended import jwt_required, get_jwt_identity

from models import Game, Publisher, Genre, Developer
from authorize_helpers import admin_required
game = Blueprint("game", __name__)


#route to list all games
@game.route("/games", methods=["GET"])
def list_games():
    try:
        # Query the database to get all games
        games = Game.query.all()

        # Serialize the games to JSON
        game_list = []
        for game in games:
            game_data = {
                'Game_ID': game.Game_ID,
                'Genre_ID': game.Genre_ID,
                'Developer_ID': game.Developer_ID,
                'Publisher_ID': game.Publisher_ID,
                'Title': game.Title,
                'Release_Date': game.Release_Date.strftime('%Y-%m-%d'),
                'Avg_User_Rating': game.Avg_User_Rating,
                'Num_User_Rating': game.Num_User_Rating,
            }
            game_list.append(game_data)

        return jsonify(game_list)

    except Exception as e:
        return jsonify({'error': 'An error occurred while fetching games.'}), 500
    


#route to list game by ID
@game.route("/games/<int:Game_ID>", methods=["GET"])
def read_game(Game_ID):
    try:
        # Query the database to get the game by Game_ID
        game = Game.query.get(Game_ID)

        # Check if the game exists
        if game is None:
            return jsonify({'error': 'Game not found'}), 404

        # Serialize the game data to JSON
        game_data = {
            'Game_ID': game.Game_ID,
            'Genre_ID': game.Genre_ID,
            'Developer_ID': game.Developer_ID,
            'Publisher_ID': game.Publisher_ID,
            'Title': game.Title,
            'Release_Date': game.Release_Date.strftime('%Y-%m-%d'),
            'Avg_User_Rating': game.Avg_User_Rating,
            'Num_User_Rating': game.Num_User_Rating,
        }

        return jsonify(game_data)

    except Exception as e:
        return jsonify({'error': 'An error occurred while fetching the game.'}), 500


#list game by genre ID
@game.route("/games/genre/<int:Genre_ID>", methods=["GET"])
def filter_game_by_genre(Genre_ID):
    try:
        #query database to show games with a specific Genre_ID
        games = Genre.query.filter_by(Genre_ID=Genre_ID).all()

        #serialize the games to json
        game_list = []
        for game in games:
            game_data = {
                'Game_ID': game.Game_ID,
                'Genre_ID': game.Genre_ID,
                'Developer_ID': game.Developer_ID,
                'Publisher_ID': game.Publisher_ID,
                'Title': game.Title,
                'Release_Date': game.Release_Date.strftime('%Y-%m-%d'),
                'Avg_User_Rating': game.Avg_User_Rating,
                'Num_User_Rating': game.Num_User_Rating,
            }
            game_list.append(game_data)

        return jsonify(game_list)

    except Exception as e:
        return jsonify({'error': 'An error occurred while fetching games by genre.'}), 500
    

#list games by developer ID
@game.route("/games/developer/<int:Developer_ID>", methods=["GET"])
def filter_game_by_dev(Developer_ID):
    try:
        #query database to show games with a specific Developer_ID
        games = Developer.query.filter_by(Developer_ID=Developer_ID).all()

        #serialize the games to json
        game_list = []
        for game in games:
            game_data = {
                'Game_ID': game.Game_ID,
                'Genre_ID': game.Genre_ID,
                'Developer_ID': game.Developer_ID,
                'Publisher_ID': game.Publisher_ID,
                'Title': game.Title,
                'Release_Date': game.Release_Date.strftime('%Y-%m-%d'),
                'Avg_User_Rating': game.Avg_User_Rating,
                'Num_User_Rating': game.Num_User_Rating,
            }
            game_list.append(game_data)

        return jsonify(game_list)

    except Exception as e:
        return jsonify({'error': 'An error occurred while fetching games by developer.'}), 500
    

#list games by developer ID
@game.route("/games/publisher/<int:Publisher_ID>", methods=["GET"])
def filter_game_by_publisher(Publisher_ID):
    try:
        #query database to show games with a specific Developer_ID
        games = Publisher.query.filter_by(Publisher_ID=Publisher_ID).all()

        #serialize the games to json
        game_list = []
        for game in games:
            game_data = {
                'Game_ID': game.Game_ID,
                'Genre_ID': game.Genre_ID,
                'Developer_ID': game.Developer_ID,
                'Publisher_ID': game.Publisher_ID,
                'Title': game.Title,
                'Release_Date': game.Release_Date.strftime('%Y-%m-%d'),
                'Avg_User_Rating': game.Avg_User_Rating,
                'Num_User_Rating': game.Num_User_Rating,
            }
            game_list.append(game_data)

        return jsonify(game_list)

    except Exception as e:
        return jsonify({'error': 'An error occurred while fetching games by genre.'}), 500
    

# Delete game by ID
@game.route('/games/<int:Game_ID>', methods=['DELETE'])
@jwt_required()
@admin_required() 
def delete_game(Game_ID):
    try:
        # Query the database to get the game by Game_ID
        game = Game.query.get(Game_ID)

        # Check if the game exists
        if game is None:
            return jsonify({'error': 'Game not found'}), 404

        # Delete the game
        db.session.delete(game)
        db.session.commit()

        return jsonify({'message': 'Game deleted successfully'})

    except Exception as e:
        return jsonify({'error': 'An error occurred while deleting the game.'}), 500