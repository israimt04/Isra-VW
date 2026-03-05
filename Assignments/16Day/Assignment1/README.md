# Flask Product Listing App

This is a simple Flask application that displays a dynamic product listing page at `/products`.

## Features
- Filter products by category and availability using URL query parameters
- Sort products by price (low to high, high to low)
- Display total count of filtered products
- Show a message if no products match the filters

## Usage
1. Install dependencies: `pip install flask`
2. Start the server: `python app.py`
3. Visit `http://localhost:5000/products` in your browser

## Query Parameters
- `category`: Filter by product category
- `available`: Filter by availability (`true` or `false`)
- `sort`: Sort by price (`asc` for low-high, `desc` for high-low)
