from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

# JSON faylından oxuma funksiyası
def read_json(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return []

# CSV faylından oxuma funksiyası
def read_csv(file_path):
    data = []
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # id və price tip çevirməsi
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                data.append(row)
    except Exception as e:
        print(f"Error reading CSV: {e}")
    return data

@app.route('/products')
def products():
    source = request.args.get('source', '').lower()
    id_param = request.args.get('id', None)
    
    # Data oxuma
    if source == 'json':
        data = read_json('products.json')
    elif source == 'csv':
        data = read_csv('products.csv')
    else:
        return render_template('product_display.html', error="Wrong source", products=[])

    # Filter by id if provided
    if id_param:
        try:
            id_value = int(id_param)
            filtered = [item for item in data if item.get('id') == id_value]
            if not filtered:
                return render_template('product_display.html', error="Product not found", products=[])
            data = filtered
        except ValueError:
            return render_template('product_display.html', error="Invalid id parameter", products=[])

    return render_template('product_display.html', products=data, error=None)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

