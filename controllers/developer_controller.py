from flask import Blueprint, jsonify, request, abort
from flask_jwt_extended import jwt_required
from main import db
from marshmallow.exceptions import ValidationError


from .custom_decorator import admin_required
from models import Developer
from schemas import DeveloperSchema



developers = Blueprint("developers", __name__, url_prefix="/developer")

#show all developers
@developers.route("/", methods=["GET"])
def get_all_developers():
    try:
        # Query the database to retrieve all developers
        all_developers = Developer.query.all()

        # Serialize the list of developers using DeveloperSchema
        developer_schema = DeveloperSchema(many=True)
        developers_data = developer_schema.dump(all_developers)

        # Return the list of developers as JSON response
        return jsonify(developers_data), 200
    except Exception as e:
        # Handle exceptions and return an error response if needed
        return jsonify({"message": "An error occurred"}), 500


#show developer by id number
@developers.route("/<int:developer_id>", methods=["GET"])
def get_developer_by_id(developer_id):
    try:
        # Query the database to retrieve a developer by their ID
        developer = Developer.query.get(developer_id)

        if not developer:
            return abort(404, description="Developer not found")

        # Serialize the developer using DeveloperSchema
        developer_schema = DeveloperSchema()
        developer_data = developer_schema.dump(developer)

        # Return the developer data as a JSON response
        return jsonify(developer_data), 200
    except Exception as e:
        # Handle exceptions and return an error response if needed
        return jsonify({"message": "An error occurred"}), 500


#route to update a developer by id, admin only
@developers.route("/<int:developer_id>", methods=["PUT", "PATCH"])
@jwt_required()  
@admin_required
def update_developer(developer_id):
    # Query the database to retrieve the developer by their ID
    developer = Developer.query.get(developer_id)

    if not developer:
        return abort(404, description="Developer not found")

    # Parse the incoming JSON data for updates
    developer_schema = DeveloperSchema()
    developer_data = request.json

    try:
        # Determine the HTTP method used (PUT or PATCH) and perform the update accordingly
        if request.method == "PUT":
            # For PUT requests, replace the entire developer with the new data
            developer_schema.load(developer_data, instance=developer)
        elif request.method == "PATCH":
            # For PATCH requests, apply partial updates to the developer
            developer_schema.load(developer_data, instance=developer, partial=True)

        db.session.commit()

    except ValidationError as err:
        # Construct a custom error response with detailed error messages
        error_messages = []
        for field, errors in err.messages.items():
            for error in errors:
                error_messages.append(f"Invalid value for '{field}': {error}")#remember to make error messages at a late date

        return jsonify({"errors": error_messages}), 400

    # Serialize and return the updated developer data
    updated_developer_data = developer_schema.dump(developer)
    return jsonify(updated_developer_data), 200





#create a new developer,admin only
@developers.route("/create", methods=["POST"])
@jwt_required()
@admin_required
def create_developer():
    try:
        # Parse the incoming JSON data using DeveloperSchema
        developer_schema = DeveloperSchema()
        developer_data = request.json

        # Validate the data and load it into a Developer object
        developer = developer_schema.load(developer_data)

        # Create a new developer object and add it to the database
        new_developer = Developer(
            name=developer.name,
            website=developer.website,
            contact_info=developer.contact_info
        )

        db.session.add(new_developer)
        db.session.commit()

        # Return the created developer data, including the assigned developer_id
        created_developer_data = developer_schema.dump(new_developer)
        return jsonify(created_developer_data), 201
    
    except ValidationError as err:
        #handl the validation errors and return an error response
        return jsonify(err.messages), 400



#deleteing a developer
@developers.route("/<int:developer_id>", methods=["DELETE"])
@jwt_required()
@admin_required  
def delete_developer_by_id(developer_id):
    try:
        # Query the database to retrieve the developer by their ID
        developer = Developer.query.get(developer_id)

        if not developer:
            return abort(404, description="Developer not found")

        # Delete the developer from the database
        db.session.delete(developer)
        db.session.commit()

        #return a success message indicating that the developer has been deleted
        return jsonify({"message": "Developer deleted successfully"}), 200
    
    except Exception as e:
        # Return a success message indicating that the developer has been deleted
        return jsonify({"message": "Developer deleted successfully"}), 200