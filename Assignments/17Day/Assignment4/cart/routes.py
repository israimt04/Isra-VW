from flask import render_template, request, redirect, make_response
from cart import cart_bp
import json

PRODUCTS = {
    "laptop": 50000,
    "mouse": 500,
    "keyboard": 1500,
    "monitor": 12000,
    "headphones": 2000
}

@cart_bp.route("/")
def view_cart():
    cart = request.cookies.get("cart")

    if not cart:
        return render_template("cart.html", empty=True)

    cart = json.loads(cart)

    total = 0
    for item, qty in cart.items():
        total += PRODUCTS[item] * qty

    return render_template("cart.html", cart=cart, prices=PRODUCTS, total=total)


@cart_bp.route("/increase/<item>")
def increase(item):
    cart = json.loads(request.cookies.get("cart"))
    cart[item] += 1

    response = make_response(redirect("/cart"))
    response.set_cookie("cart", json.dumps(cart))
    return response


@cart_bp.route("/decrease/<item>")
def decrease(item):
    cart = json.loads(request.cookies.get("cart"))
    cart[item] -= 1

    if cart[item] <= 0:
        del cart[item]

    response = make_response(redirect("/cart"))
    response.set_cookie("cart", json.dumps(cart))
    return response


@cart_bp.route("/clear")
def clear_cart():
    response = make_response(redirect("/cart"))
    response.delete_cookie("cart")
    return response