from flask import Flask, render_template, request
import sqlite3
import csv
import json
import os

app = Flask(__name__)

# Sample data for JSON and CSV
products_data = [
    {"id": 1, "name": "Laptop", "price": 799.99, "category": "Electronics"},
    {"id": 2, "name": "Coffee Mug", "price": 15.99, "category": "Home Goods"}
]

CSV_FILE = 'products.csv'

# Optional: create a CSV file if not exists
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["id", "name", "price", "category"])
        writer.writeheader()
        for product in products_data:
            writer.writerow(product)

def get_products_from_db():
    """Fetch products from SQLite database"""
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, price, category FROM Products")
        rows = cursor.fetchall()
        conn.close()
        # Convert to list of dicts for template rendering
        return [{"id": r[0], "name": r[1], "price": r[2], "category": r[3]} for r in rows]
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []

@app.route('/products')
def display_products():
    source = request.args.get('source', 'json').lower()

    if source == 'json':
        products = products_data
    elif source == 'csv':
        try:
            with open(CSV_FILE, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                products = [row for row in reader]
                # Convert price to float
                for p in products:
                    p['price'] = float(p['price'])
        except Exception as e:
            return f"Error reading CSV file: {e}", 500
    elif source == 'sql':
        products = get_products_from_db()
        if not products:
            return "Database error or no products found", 500
    else:
        return "Wrong source", 400

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
