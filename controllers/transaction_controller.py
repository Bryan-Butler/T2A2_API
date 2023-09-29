from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity,current_user

from models import Transactions
from schemas import TransactionSchema
from custom_decorator import admin_required
from main import db



# Create a Blueprint for the transaction routes
transaction = Blueprint('transaction', __name__, url_prefix="/transaction")


#route to make a new transaction as yourself
@transaction.route("/", methods=["POST"])
@jwt_required() 
def create_transaction():
    try:
        # Get the current user's identity from the JWT token
        current_user_id = get_jwt_identity()

        # Parse the incoming JSON data using TransactionSchema
        transaction_schema = TransactionSchema()
        transaction_data = request.json

        # Create a new transaction object
        new_transaction = Transactions(
            user_id=current_user_id,
            game_id=transaction_data['game_id'],
            purchase_date=transaction_data['purchase_date'],
            transaction_amount=transaction_data['transaction_amount'],
            payment_method=transaction_data['payment_method'],
            transaction_status=transaction_data['transaction_status']
        )

        # Add the new transaction to the database
        db.session.add(new_transaction)
        db.session.commit()

        # Return the created transaction data, including the assigned transaction_id
        created_transaction_data = transaction_schema.dump(new_transaction)
        return jsonify(created_transaction_data), 201

    except Exception as e:
        # Handle exceptions and return an error response if needed
        return jsonify({"message": "An error occurred"}), 500
    


# Route to get all transactions for the current user (JWT required)
@transaction.route("/", methods=["GET"])
@jwt_required()
def get_user_transactions():
    try:
        # Get the current user's identity from the JWT token
        current_user_id = get_jwt_identity()

        # Query the database to retrieve all transactions for the current user
        user_transactions = Transactions.query.filter_by(user_id=current_user_id).all()

        # Serialize the list of transactions using TransactionSchema
        transaction_schema = TransactionSchema(many=True)
        transaction_data = transaction_schema.dump(user_transactions)

        # Return the list of transactions for the current user as a JSON response
        return jsonify(transaction_data), 200

    except Exception as e:
        # Handle exceptions and return an error response if needed
        return jsonify({"message": "An error occurred"}), 500
    


#lets the logged in user view their own transactions by transaction id
@transaction.route("/<int:transaction_id>", methods=["GET"])
@jwt_required() 
def get_transaction_by_id(transaction_id):
    try:
        # Get the current user's identity from the JWT token
        current_user_id = get_jwt_identity()

        # Query the database to retrieve the transaction by its ID
        transaction = Transactions.query.get(transaction_id)

        # Check if the transaction exists and belongs to the current user
        if not transaction:
            return jsonify({"message": "Transaction not found"}), 404
        if transaction.user_id != current_user_id:
            return jsonify({"message": "Permission denied. This is not your transaction"}), 403

        # Serialize the transaction using TransactionSchema
        transaction_schema = TransactionSchema()
        transaction_data = transaction_schema.dump(transaction)

        # Return the transaction data as a JSON response
        return jsonify(transaction_data), 200

    except Exception as e:
        # Handle exceptions and return an error response if needed
        return jsonify({"message": "An error occurred"}), 500
    

#route for admin to update transactions
@transaction.route("/<int:transaction_id>", methods=["PUT", "PATCH"])
@jwt_required() 
@admin_required() 
def update_transaction(transaction_id):
    try:
        # Query the database to retrieve the transaction by its ID
        transaction = Transactions.query.get(transaction_id)

        if not transaction:
            return jsonify({"message": "Transaction not found"}), 404

        # Parse the JSON data from the request to update the transaction fields
        data = request.get_json()

        # Update the transaction fields based on the incoming data
        if "purchase_date" in data:
            transaction.purchase_date = data["purchase_date"]
        if "transaction_amount" in data:
            transaction.transaction_amount = data["transaction_amount"]
        if "payment_method" in data:
            transaction.payment_method = data["payment_method"]
        if "transaction_status" in data:
            transaction.transaction_status = data["transaction_status"]

        # Commit the changes to the database
        db.session.commit()

        # Return a success message indicating that the transaction has been updated
        return jsonify({"message": "Transaction updated successfully"}), 200

    except Exception as e:
        # Handle exceptions and return an error response if needed
        return jsonify({"message": "An error occurred"}), 500
    


#route for admin to delete a transaction if needed
@transaction.route("/<int:transaction_id>", methods=["DELETE"])
@jwt_required()  
@admin_required() 
def delete_transaction(transaction_id):
    try:
        # Query the database to retrieve the transaction by its ID
        transaction = Transactions.query.get(transaction_id)

        if not transaction:
            return jsonify({"message": "Transaction not found"}), 404

        # Delete the transaction from the database
        db.session.delete(transaction)
        db.session.commit()

        # Return a success message indicating that the transaction has been deleted
        return jsonify({"message": "Transaction deleted successfully"}), 200

    except Exception as e:
        # Handle exceptions and return an error response if needed
        return jsonify({"message": "An error occurred"}), 500
    

#route for admin to view all transactions
@transaction.route("/all_transaction", methods=["GET"])
@jwt_required()  
@admin_required()
def get_all_transactions():
    try:
        # Query the database to retrieve all transactions
        all_transactions = Transactions.query.all()

        # Serialize the list of transactions using TransactionSchema
        transaction_schema = TransactionSchema(many=True)
        transaction_data = transaction_schema.dump(all_transactions)

        # Return the list of transactions as a JSON response
        return jsonify(transaction_data), 200

    except Exception as e:
        # Handle exceptions and return an error response if needed
        return jsonify({"message": "An error occurred"}), 500