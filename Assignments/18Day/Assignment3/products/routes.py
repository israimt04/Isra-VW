from flask import Blueprint, jsonify, session, request, make_response
import json

products_bp = Blueprint('products', __name__, url_prefix='/products')

products = [
    {"id": 1, "name": "Laptop", "price": 70000},
    {"id": 2, "name": "Mouse", "price": 500},
    {"id": 3, "name": "Keyboard", "price": 1200}
]

# API 2: Get all products
@products_bp.route('/', methods=['GET'])
def get_products():
    return jsonify(products)


# API 3: View product
@products_bp.route('/<int:product_id>', methods=['GET'])
def view_product(product_id):

    if "username" not in session:
        return jsonify({"error": "User not logged in"}), 401

    product = next((p for p in products if p["id"] == product_id), None)

    if not product:
        return jsonify({"error": "Product not found"}), 404

    recent = request.cookies.get("recent_products")

    if recent:
        recent_products = json.loads(recent)
    else:
        recent_products = []

    if product_id in recent_products:
        recent_products.remove(product_id)

    recent_products.insert(0, product_id)

    if len(recent_products) > 5:
        recent_products = recent_products[:5]

    resp = make_response(jsonify(product))
    resp.set_cookie("recent_products", json.dumps(recent_products))

    return resp


# API 4: Recently viewed products
@products_bp.route('/recent', methods=['GET'])
def recent_products():

    recent = request.cookies.get("recent_products")

    if not recent:
        return jsonify([])

    ids = json.loads(recent)

    result = []

    for pid in ids:
        product = next((p for p in products if p["id"] == pid), None)
        if product:
            result.append({
                "id": product["id"],
                "name": product["name"]
            })

    return jsonify(result)