from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow requests from different origins (like your React frontend)

# In-memory storage for form data (simulating a database)
orders = []

# POST route to handle form submission from React
@app.route('/submit-form', methods=['POST'])
def submit_form():
    data = request.json  # Retrieve JSON data from the request
    orders.append(data)  # Append the new order to the in-memory list
    return jsonify({'message': 'Form submitted successfully!', 'data': data}), 200

# GET route to fetch all orders (for testing purposes)
@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders), 200  # Return all the orders in JSON format

# Main entry point to run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
