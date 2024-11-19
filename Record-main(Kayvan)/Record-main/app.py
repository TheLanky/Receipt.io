# app.py
from flask import Flask, request, jsonify
from ocr_service import extract_text
from categorization_service import categorize_receipt
from parser import parse_response
from Receipt_App_CRUD import create_receipt, create_item, read_receipts, read_items, close_connection, update_receipt, delete_receipt
from auth import sign_in, sign_up
import uuid
import re
def clean_currency(value):
    """
    Cleans and converts a value to a float. Handles strings, floats, integers, and None values.

    :param value: The value to clean (string, float, int, or None).
    :return: A float value.
    :raises: TypeError if the value is not a supported type.
    """
    if value is None:  # Handle None as a special case
        return 0.0
    elif isinstance(value, (float, int)):  # Return numeric types as-is
        return float(value)
    elif isinstance(value, str):  # Process strings
        cleaned_value = re.sub(r'[^\d.]+', '', value)  # Remove non-numeric characters except '.'
        return float(cleaned_value) if cleaned_value else 0.0
    else:
        raise TypeError(f"Expected string, float, int, or None, got {type(value)}")
app = Flask(__name__)
@app.route('/')
def home():
    return "Welcome to the Receipt Manager App!"



# Authentication Endpoints

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    phone = data.get('phone')

    if sign_up(email, password, phone):
        return jsonify({"message": f"User {email} registered successfully!"}), 201
    else:
        return jsonify({"error": "Sign-up failed."}), 400

@app.route('/signin', methods=['POST'])
def signin():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    user_id = sign_in(email, password)  # This calls the sign_in function from auth.py
    if user_id:
        return jsonify({"message": "Signed in successfully", "user_id": user_id}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

# OCR Extraction Endpoint
@app.route('/extract', methods=['POST'])
def extract_text_from_image():
    image_file = request.files['image']  # Get the uploaded image file from the request
    image_path = f"./uploads/{image_file.filename}"  # Save the image in a folder named 'uploads'
    image_file.save(image_path)  # Save the file to the server

    # Extract text using the OCR service
    receipt_text = extract_text(image_path)

    # Return the extracted text as a JSON response
    return jsonify({"receipt_text": receipt_text}), 200

# Categorize and Parse Receipt
@app.route('/categorize', methods=['POST'])
def categorize_and_parse():
    data = request.json
    receipt_text = data.get('receipt_text')  # Get the receipt text from the request
    response_text = categorize_receipt(receipt_text)  # Categorize the receipt using the categorization service

    receipt, items = parse_response(response_text)  # Parse the categorized response
    if receipt and items:
        return jsonify({"receipt": receipt, "items": items}), 200  # Return the parsed receipt and items
    else:
        return jsonify({"error": "Parsing failed"}), 400
@app.route('/receipts', methods=['POST'])
def create_receipt_with_items():

    data = request.json  # Get the incoming JSON data from the request
    user_id = data.get('user_id')  # User ID from the request
    receipt_data = data.get('receipt')  # Receipt data from the request
    items_data = data.get('items')  # Items data from the request

    receipt_id = str(uuid.uuid4())  # Generate a unique ID for the receipt
    vendor = receipt_data.get('vendor')
    receipt_date = receipt_data.get('receipt_date')
    total = clean_currency(receipt_data.get('total'))  # Clean the currency values
    total_amount_given = clean_currency(receipt_data.get('total_amount_given'))
    change = clean_currency(receipt_data.get('change'))
    payment_method = receipt_data.get('payment_method')

    # Call the function to insert the receipt into the database
    create_receipt(user_id, receipt_id, vendor, receipt_date, total, total_amount_given, change, payment_method)

    # Insert each item in the items list into the database
    for item in items_data:
        create_item(receipt_id, item["Item name"], item["Amount"], item.get("Category", "Uncategorized"))

    # Return a success message
    return jsonify({"message": f"Receipt {receipt_id} created successfully!"}), 201

# Retrieve Receipts
@app.route('/receipts', methods=['GET'])
def get_receipts():
    user_id = request.args.get('user_id')

    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    receipts = read_receipts(user_id)

    if not receipts:
        return jsonify({"message": "No receipts found for the user"}), 404

    return jsonify({"receipts": receipts}), 200


# Retrieve Items for a Receipt
@app.route('/receipts/<receipt_id>/items', methods=['GET'])
def get_items(receipt_id):
    if not receipt_id:
        return jsonify({"error": "Receipt ID is required"}), 400

    items = read_items(receipt_id)

    if not items:
        return jsonify({"message": "No items found for the receipt"}), 404

    return jsonify({"items": items}), 200
#Update receipt
@app.route('/receipts/<receipt_id>', methods=['PUT'])
def update_receipt_details(receipt_id):
    data = request.json
    vendor = data.get('vendor')
    receipt_date = data.get('receipt_date')
    total_amount_given = clean_currency(data.get('total_amount_given'))
    change = clean_currency(data.get('change'))
    payment_method = data.get('payment_method')

    update_receipt(receipt_id, vendor, receipt_date, total_amount_given, change, payment_method)
    return jsonify({"message": f"Receipt {receipt_id} updated successfully!"}), 200
#Delete receipt
@app.route('/receipts/<receipt_id>', methods=['DELETE'])
def remove_receipt(receipt_id):
    delete_receipt(receipt_id)
    return jsonify({"message": f"Receipt {receipt_id} and its associated items deleted successfully!"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
