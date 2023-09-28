from flask import Blueprint, jsonify, request, abort
from flask_jwt_extended import jwt_required
from main import db
from marshmallow.exceptions import ValidationError

from custom_decorator import admin_required
from models import Publisher
from schemas import PublisherSchema


publisher = Blueprint('publisher_bp', __name__, url_prefix="/publisher")

#show all publishers
@publisher.route("/", methods=["GET"])
def get_all_publishers():
    try:
        # Query the database to retrieve all publishers
        all_publishers = Publisher.query.all()

        # Serialize the list of publishers using PublisherSchema
        publisher_schema = PublisherSchema(many=True)
        publisher_data = publisher_schema.dump(all_publishers)

        # Return the list of publishers as a JSON response
        return jsonify(publisher_data), 200
    except Exception as e:
        # Handle exceptions and return an error response if needed
        return jsonify({"message": "An error occurred"}), 500



#show publisher by id number
@publisher.route("/<int:publisher_id>", methods=["GET"])
def get_publisher_by_id(publisher_id):
    try:
        # Query the database to retrieve a publisher by their ID
        publisher = Publisher.query.get(publisher_id)

        if not publisher:
            return abort(404, description="Publisher not found")

        # Serialize the publisher using PublisherSchema
        publisher_schema = PublisherSchema()
        publisher_data = publisher_schema.dump(publisher)

        # Return the publisher data as a JSON response
        return jsonify(publisher_data), 200
    except Exception as e:
        # Handle exceptions and return an error response if needed
        return jsonify({"message": "An error occurred"}), 500
    


#route to update info by publisher id, admin only
@publisher.route("/<int:publisher_id>", methods=["PUT", "PATCH"])
@jwt_required()
@admin_required()
def update_publisher(publisher_id):
    # Query the database to retrieve the publisher by their ID
    publisher = Publisher.query.get(publisher_id)

    if not publisher:
        return abort(404, description="Publisher not found")

    # Parse the incoming JSON data for updates
    schema = PublisherSchema()
    publisher_data = request.json

    try:
    # Determine the HTTP method used (PUT or PATCH) and perform the update accordingly
        if request.method == "PUT":
            # For PUT requests, replace the entire publisher with the new data
            schema.load(publisher_data, instance=publisher)
        elif request.method == "PATCH":
            # For PATCH requests, apply partial updates to the publisher
            schema.load(publisher_data, instance=publisher, partial=True)

        db.session.commit()

    except ValidationError as err:
        # Construct a custom error response with detailed error messages
        error_messages = []
        for field, errors in err.messages.items():
            for error in errors:
                error_messages.append(f"Invalid value for '{field}': {error}")

        return jsonify({"errors": error_messages}), 400

    # Serialize and return the updated publisher data
    updated_publisher_data = schema.dump(publisher)
    return jsonify(updated_publisher_data), 200


#create a new publisher, admin only
@publisher.route("/create", methods=["POST"])
@jwt_required()
@admin_required 
def create_publisher():
    try:
        # Parse the incoming JSON data using PublisherSchema
        publisher_schema = PublisherSchema()
        publisher_data = request.json

        # Validate the data and load it into a Publisher object
        publisher = publisher_schema.load(publisher_data)

        # Create a new publisher object and add it to the database
        new_publisher = Publisher(
            name=publisher.name,
            website=publisher.website,
            contact_info=publisher.contact_info
        )

        db.session.add(new_publisher)
        db.session.commit()

        # Return the created publisher data, including the assigned publisher_id
        created_publisher_data = publisher_schema.dump(new_publisher)
        return jsonify(created_publisher_data), 201

    except ValidationError as err:
        # Handle validation errors and return an error response
        return jsonify(err.messages), 400



#route to delete publisher by id, admin only
@publisher.route("/<int:publisher_id>", methods=["DELETE"])
@jwt_required()
@admin_required 
def delete_publisher_by_id(publisher_id):
    try:
        # Query the database to retrieve the publisher by their ID
        publisher = Publisher.query.get(publisher_id)

        if not publisher:
            return abort(404, description="Publisher not found")

        # Delete the publisher from the database
        db.session.delete(publisher)
        db.session.commit()

        # Return a success message indicating that the publisher has been deleted
        return jsonify({"message": "Publisher deleted successfully"}), 200

    except Exception as e:
        # Handle exceptions and return an error response if needed
        return jsonify({"message": "An error occurred"}), 500