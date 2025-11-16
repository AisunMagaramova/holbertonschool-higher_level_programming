from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# JSON faylından oxuma
def read_json(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return []

# CSV faylından oxuma
def read_csv(file_path):
    data = []
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                data.append(row)
    except Exception as e:
        print(f"Error reading CSV: {e}")
    return data

# SQLite-dan oxuma
def read_sqlite(db_file):
    data = []
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            data.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })
        conn.close()
    except Exception as e:
        print(f"Error reading SQLite DB: {e}")
    return data

@app.route('/products')
def products():
    source = request.args.get('source', '').lower()
    id_param = request.args.get('id', None)

    # Data oxuma mənbələrinə görə
    if source == 'json':
        data = read_json('products.json')
    elif source == 'csv':
        data = read_csv('products.csv')
    elif source == 'sql':
        data = read_sqlite('products.db')
    else:
        return render_template('product_display.html', error="Wrong source", products=[])

    # Filter by id if provided
    if id_param:
        try:
            id_value = int(id_param)
            filtered = [item for item in data if item.get('id') == id_value]
            if not filtered:
                return render_template('product_display.html', error="Product not fou

