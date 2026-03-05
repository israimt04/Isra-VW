from flask import render_template
from orders import orders_bp

@orders_bp.route("/")
def orders_page():
    return render_template("orders.html")