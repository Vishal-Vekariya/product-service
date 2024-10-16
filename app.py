from flask import Flask, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

app = Flask(__name__)

# Enable CORS for all origins and only allow GET methods
CORS(app, resources={r"/products": {"origins": "*"}}, methods=['GET'])

# Define the products route
@app.route('/products', methods=['GET'])
def get_products():
    # Define a list of product dictionaries
    products = [
        {"id": 1, "name": "Dog Food", "price": 19.99},
        {"id": 2, "name": "Cat Food", "price": 34.99},
        {"id": 3, "name": "Bird Seeds", "price": 10.99}
    ]
    # Return the list as a JSON response
    return jsonify(products)

if __name__ == '__main__':
    # Get the port from environment variables or default to 3030
    port = int(os.getenv('PORT', 3030))
    # Run the Flask app on all interfaces with the specified port
    app.run(host='0.0.0.0', port=port)
