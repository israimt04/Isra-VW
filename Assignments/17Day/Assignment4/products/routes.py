from flask import render_template, request, redirect, make_response
from products import products_bp
import json

# Dummy Products
PRODUCTS = {
    "laptop": 50000,
    "mouse": 500,
    "keyboard": 1500,
    "monitor": 12000,
    "headphones": 2000
}

@products_bp.route("/")
def product_list():
    return render_template("products.html", products=PRODUCTS)

@products_bp.route("/add/<product>")
def add_to_cart(product):
    cart = request.cookies.get("cart")

    if cart:
        cart = json.loads(cart)
    else:
        cart = {}

    if product in cart:
        cart[product] += 1
    else:
        cart[product] = 1

    response = make_response(redirect("/cart"))
    response.set_cookie("cart", json.dumps(cart))

    return response