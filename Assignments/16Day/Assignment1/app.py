from flask import Flask, render_template, request

app = Flask(__name__)

# In-memory product data
PRODUCTS = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 1200, "available": True},
    {"id": 2, "name": "Desk Chair", "category": "Furniture", "price": 150, "available": False},
    {"id": 3, "name": "Monitor", "category": "Electronics", "price": 300, "available": True},
    {"id": 4, "name": "Coffee Table", "category": "Furniture", "price": 90, "available": True},
    {"id": 5, "name": "Notebook", "category": "Stationery", "price": 5, "available": True},
    {"id": 6, "name": "Pen", "category": "Stationery", "price": 2, "available": False},
]

@app.route('/products')
def products():
    category = request.args.get('category')
    available = request.args.get('available')
    sort = request.args.get('sort')

    filtered = PRODUCTS
    if category:
        filtered = [p for p in filtered if p['category'].lower() == category.lower()]
    if available is not None:
        if available.lower() == 'true':
            filtered = [p for p in filtered if p['available']]
        elif available.lower() == 'false':
            filtered = [p for p in filtered if not p['available']]
    if sort == 'asc':
        filtered = sorted(filtered, key=lambda x: x['price'])
    elif sort == 'desc':
        filtered = sorted(filtered, key=lambda x: x['price'], reverse=True)

    total = len(filtered)
    return render_template('products.html', products=filtered, total=total)

if __name__ == '__main__':
    app.run(debug=True)
