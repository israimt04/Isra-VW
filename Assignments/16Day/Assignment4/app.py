from flask import Flask, render_template, request

app = Flask(__name__)

students = [
    {"name": "John", "marks": 80},
    {"name": "amit", "marks": 70},
]

products = [
    {"name": "Laptop", "category": "Electronics", "price": 1200.00, "available": True},
    {"name": "Desk Chair", "category": "Furniture", "price": 150.00, "available": False},
    {"name": "Monitor", "category": "Electronics", "price": 300.00, "available": True},
    {"name": "Notebook", "category": "Stationery", "price": 5.50, "available": True},
    {"name": "Pen", "category": "Stationery", "price": 1.20, "available": False},
    {"name": "Coffee Table", "category": "Furniture", "price": 80.00, "available": True},
]

@app.route("/")
def student_table():
    return render_template("students.html", students=students)

@app.route("/products")
def product_listing():
    category = request.args.get("category", "")
    available = request.args.get("available", "")
    sort = request.args.get("sort", "")

    filtered = products
    if category:
        filtered = [p for p in filtered if p["category"] == category]
    if available == "true":
        filtered = [p for p in filtered if p["available"]]
    elif available == "false":
        filtered = [p for p in filtered if not p["available"]]
    if sort == "asc":
        filtered = sorted(filtered, key=lambda x: x["price"])
    elif sort == "desc":
        filtered = sorted(filtered, key=lambda x: x["price"], reverse=True)

    categories = sorted(set(p["category"] for p in products))
    return render_template(
        "products.html",
        products=filtered,
        categories=categories,
        selected_category=category,
        selected_available=available,
        sort=sort
    )

if __name__ == "__main__":
    app.run(debug=True)