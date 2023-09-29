from flask import Blueprint, jsonify, request
from marshmallow.exceptions import ValidationError
from flask_jwt_extended import jwt_required, get_jwt_identity

from models import Review, User, Game
from schemas import ReviewSchema
from custom_decorator import admin_required
from main import db




review = Blueprint("review", __name__, url_prefix="/review")

#route to view all reviews for a game by game_id
@review.route("/game/<int:game_id>", methods=["GET"])
def get_reviews_by_game_id(game_id):
    try:
        # Query the database to retrieve all reviews with the specified game_id
        reviews = Review.query.filter_by(game_id=game_id).all()

        # Serialize the list of reviews using ReviewSchema
        review_schema = ReviewSchema(many=True)
        review_data = review_schema.dump(reviews)

        # Return the list of reviews as JSON
        return jsonify(review_data), 200

    except Exception as e:
        # Handle exceptions and return an error response if needed
        return jsonify({"message": "An error occurred"}), 500




#route to view all reviews from a user by user_id
@review.route("/user/<int:user_id>", methods=["GET"])
def get_reviews_by_user_id(user_id):
    try:
        # Query the database to retrieve all reviews with the specified user_id
        reviews = Review.query.filter_by(user_id=user_id).all()

        # Serialize the list of reviews using ReviewSchema
        review_schema = ReviewSchema(many=True)
        review_data = review_schema.dump(reviews)

        # Return the list of reviews as JSON
        return jsonify(review_data), 200

    except Exception as e:
        # Handle exceptions and return an error response if needed
        return jsonify({"message": "An error occurred"}), 500




#route to update a review as a user by review_id
@review.route("/<int:review_id", methods=["PUT", "PATCH"])
@jwt_required()  
def update_review(review_id):
    try:
        # Parse the incoming JSON data using ReviewSchema
        review_schema = ReviewSchema()
        review_data = request.json

        # Retrieve the review by its ID
        review = Review.query.get(review_id)

        # Check if the review exists
        if not review:
            return jsonify({"message": "Review not found"}), 404

        # Get the current user's identity from the JWT token
        current_user_id = get_jwt_identity()

        # Check if the authenticated user is the owner of the review
        if review.user_id != current_user_id:
            return jsonify({"message": "Permission denied. You can only update your own reviews"}), 403

        # Update the review attributes (rating and/or review_description)
        if 'rating' in review_data:
            review.rating = review_data['rating']
        if 'review_description' in review_data:
            review.review_description = review_data['review_description']

        db.session.commit()

        # Serialize and return the updated review data as JSON
        updated_review_data = review_schema.dump(review)
        return jsonify(updated_review_data), 200

    except ValidationError as err:
        # Handle validation errors and return an error response
        return jsonify(err.messages), 400




#route to delete a review as the owner of the review, by review_id
@review.route("/<int:review_id>", methods=["DELETE"])
@jwt_required()  
def delete_review(review_id):
    try:
        # Retrieve the review by its ID
        review = Review.query.get(review_id)

        # Check if the review exists
        if not review:
            return jsonify({"message": "Review not found"}), 404

        # Get the current user's identity from the JWT token
        current_user_id = get_jwt_identity()

        # Check if the authenticated user is the owner of the review or an admin (if necessary)
        if review.user_id != current_user_id:
            return jsonify({"message": "Permission denied. You can only delete your own reviews"}), 403

        # Delete the review from the database
        db.session.delete(review)
        db.session.commit()

        # Return a success message indicating that the review has been deleted
        return jsonify({"message": "Review deleted successfully"}), 200

    except Exception as e:
        # Handle exceptions and return an error response if needed
        return jsonify({"message": "An error occurred"}), 500



#route to create a new review
@review.route("/", methods="POST")
@jwt_required()  
def create_review():
    try:
        # Parse the incoming JSON data using ReviewSchema
        review_schema = ReviewSchema()
        review_data = request.json

        # Validate the data and load it into a Review object
        review = review_schema.load(review_data)

        # Get the current user's identity from the JWT token
        current_user_id = get_jwt_identity()

        # Check if the user exists
        user = User.query.get(current_user_id)
        if not user:
            return jsonify({"message": "User not found"}), 404

        # Check if the game exists
        game = Game.query.get(review.game_id)
        if not game:
            return jsonify({"message": "Game not found"}), 404

        # Create a new review object and add it to the database
        new_review = Review(
            user_id=current_user_id,
            game_id=review.game_id,
            rating=review.rating,
            review_description=review.review_description
        )

        db.session.add(new_review)
        db.session.commit()

        # Return the created review data as JSON with a 201 status code
        created_review_data = review_schema.dump(new_review)
        return jsonify(created_review_data), 201

    except ValidationError as err:
        # Handle validation errors and return an error response
        return jsonify(err.messages), 400
    



#route for admin to delete a review
@review.route("/admin_delete/<int:review_id>", methods=["DELETE"])
@jwt_required()  
@admin_required()  
def delete_review_as_admin(review_id):
    try:
        # Retrieve the review by its ID
        review = Review.query.get(review_id)

        # Check if the review exists
        if not review:
            return jsonify({"message": "Review not found"}), 404

        # Delete the review from the database
        db.session.delete(review)
        db.session.commit()

        # Return a success message indicating that the review has been deleted
        return jsonify({"message": "Review deleted successfully"}), 200

    except Exception as e:
        # Handle exceptions and return an error response if needed
        return jsonify({"message": "An error occurred"}), 500