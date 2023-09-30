from flask import Blueprint, jsonify
from main import db
from flask_jwt_extended import jwt_required

from models import Game, Publisher, Genre, Developer
from .custom_decorator import admin_required


game = Blueprint("game", __name__, url_prefix="/games")


#route to list all games
@game.route("/", methods=["GET"])
def list_games():
    try:
        # Query the database to get all games
        games = Game.query.all()

        # Serialize the games to JSON
        game_list = []
        for game in games:
            game_data = {
                'game_id': game.game_id,
                'genre_id': game.genre_id,
                'developer_id': game.developer_id,
                'publisher_id': game.publisher_id,
                'title': game.title,
                'release_date': game.release_date.strftime('%Y-%m-%d'),
                'avg_user_rating': game.avg_user_rating,
                'num_user_rating': game.num_user_rating,
            }
            game_list.append(game_data)

        return jsonify(game_list)

    except Exception as e:
        return jsonify({'error': 'An error occurred while fetching games.'}), 500
    


#route to list game by ID
@game.route("/games/<int:game_id>", methods=["GET"])
def read_game(game_id):
    try:
        # Query the database to get the game by game_id
        game = Game.query.get(game_id)

        # Check if the game exists
        if game is None:
            return jsonify({'error': 'Game not found'}), 404

        # Serialize the game data to JSON
        game_data = {
            'game_id': game.game_id,
            'genre_id': game.genre_id,
            'developer_id': game.developer_id,
            'publisher_id': game.publisher_id,
            'title': game.title,
            'release_date': game.release_date.strftime('%Y-%m-%d'),
            'avg_user_rating': game.avg_user_rating,
            'num_user_rating': game.num_user_rating,
        }

        return jsonify(game_data)

    except Exception as e:
        return jsonify({'error': 'An error occurred while fetching the game.'}), 500


#list game by genre ID
@game.route("/games/genre/<int:genre_id>", methods=["GET"])
def filter_game_by_genre(genre_id):
    try:
        #query database to show games with a specific genre_id
        games = Genre.query.filter_by(genre_id=genre_id).all()

        #serialize the games to json
        game_list = []
        for game in games:
            game_data = {
                'game_id': game.game_id,
                'genre_id': game.genre_id,
                'developer_id': game.developer_id,
                'publisher_id': game.publisher_id,
                'title': game.title,
                'release_date': game.release_date.strftime('%Y-%m-%d'),
                'avg_user_rating': game.avg_user_rating,
                'num_user_rating': game.num_user_rating,
            }
            game_list.append(game_data)

        return jsonify(game_list)

    except Exception as e:
        return jsonify({'error': 'An error occurred while fetching games by genre.'}), 500
    

#list games by developer ID
@game.route("/games/developer/<int:developer_id>", methods=["GET"])
def filter_game_by_dev(developer_id):
    try:
        #query database to show games with a specific developer_id
        games = Developer.query.filter_by(developer_id=developer_id).all()

        #serialize the games to json
        game_list = []
        for game in games:
            game_data = {
                'game_id': game.game_id,
                'genre_id': game.genre_id,
                'developer_id': game.developer_id,
                'publisher_id': game.publisher_id,
                'title': game.title,
                'release_date': game.release_date.strftime('%Y-%m-%d'),
                'avg_user_rating': game.avg_user_rating,
                'num_user_rating': game.num_user_rating,
            }
            game_list.append(game_data)

        return jsonify(game_list)

    except Exception as e:
        return jsonify({'error': 'An error occurred while fetching games by developer.'}), 500
    

#list games by developer ID
@game.route("/games/publisher/<int:publisher_id>", methods=["GET"])
def filter_game_by_publisher(publisher_id):
    try:
        #query database to show games with a specific developer_id
        games = Publisher.query.filter_by(publisher_id=publisher_id).all()

        #serialize the games to json
        game_list = []
        for game in games:
            game_data = {
                'game_id': game.game_id,
                'genre_id': game.genre_id,
                'developer_id': game.developer_id,
                'publisher_id': game.publisher_id,
                'title': game.title,
                'release_date': game.release_date.strftime('%Y-%m-%d'),
                'avg_user_rating': game.avg_user_rating,
                'num_user_rating': game.num_user_rating,
            }
            game_list.append(game_data)

        return jsonify(game_list)

    except Exception as e:
        return jsonify({'error': 'An error occurred while fetching games by genre.'}), 500
    

# Delete game by ID
@game.route('/games/<int:game_id>', methods=['DELETE'])
@jwt_required()
@admin_required
def delete_game(game_id):
    try:
        # Query the database to get the game by game_id
        game = Game.query.get(game_id)

        # Check if the game exists
        if game is None:
            return jsonify({'error': 'Game not found'}), 404

        # Delete the game
        db.session.delete(game)
        db.session.commit()

        return jsonify({'message': 'Game deleted successfully'})

    except Exception as e:
        return jsonify({'error': 'An error occurred while deleting the game.'}), 500