from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Sample local products
products = [
    {"name": "Laptop", "price": 50000},
    {"name": "Phone", "price": 20000},
    {"name": "Headphones", "price": 2000},
    {"name": "Tablet", "price": 20000}
]

# Local API
@app.route("/api/products")
def get_products():
    return jsonify(products)


# API that fetches external data
@app.route("/api/futurama")
def futurama_data():
    url = "https://api.sampleapis.com/futurama/info"
    response = requests.get(url)
    return jsonify(response.json())


if __name__ == "__main__":
    app.run(debug=True)