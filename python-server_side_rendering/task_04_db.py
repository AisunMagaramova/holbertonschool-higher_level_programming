from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# /products route-u
@app.route('/products')
def products():
    source = request.args.get('source')

    # JSON mənbəyi
    if source == 'json':
        try:
            with open('products.json', 'r') as f:
                products_data = json.load(f)
            return render_template('product_display.html', products=products_data)
        except FileNotFoundError:
            return "JSON file not found", 500
        except json.JSONDecodeError:
            return "Error parsing JSON", 500

    # CSV mənbəyi
    elif source == 'csv':
        try:
            products_data = []
            with open('products.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    # price-i float-a çevirmək
                    row['price'] = float(row['price'])
                    products_data.append(row)
            return render_template('product_display.html', products=products_data)
        except FileNotFoundError:
            return "CSV file not found", 500
        except Exception as e:
            return f"Error reading CSV: {e}", 500

    # SQLite mənbəyi
    elif source == 'sql':
        try:
            conn = sqlite3.connect('products.db')
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, category, price FROM Products")
            rows = cursor.fetchall()
            # Dictionary formatına çevir
            products_data = []
            for row in rows:
                products_data.append({
                    'id': row[0],
                    'name': row[1],
                    'category': row[2],
                    'price': row[3]
                })
            conn.close()
            return render_template('product_display.html', products=products_data)
        except sqlite3.Error as e:
            return f"Database error: {e}", 500

    # Yanlış source parametri
    else:
        return "Wrong source", 400


if __name__ == '__main__':
    app.run(debug=True)
