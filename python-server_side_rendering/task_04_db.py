#!/usr/bin/python3
"""Flask application to display data from JSON, CSV, or SQLite database."""
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json(filepath='products.json'):
    """Read and return data from JSON file."""
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None


def read_csv(filepath='products.csv'):
    """Read and return data from CSV file."""
    try:
        products = []
        with open(filepath, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # Convert id to int and price to float
                product = {
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                }
                products.append(product)
        return products
    except FileNotFoundError:
        return None
    except (ValueError, KeyError):
        return None


def read_sql(db_path='products.db'):
    """Read and return data from SQLite database."""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        conn.close()
        
        products = []
        for row in rows:
            product = {
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            }
            products.append(product)
        return products
    except sqlite3.Error:
        return None


@app.route('/products')
def products():
    """Display products from JSON, CSV, or SQLite based on source parameter."""
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    # Validate source parameter
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")
    
    # Read data based on source
    if source == 'json':
        products_list = read_json()
    elif source == 'csv':
        products_list = read_csv()
    else:  # source == 'sql'
        products_list = read_sql()
    
    # Handle file reading errors
    if products_list is None:
        return render_template('product_display.html', error="Error reading data")
    
    # Filter by id if provided
    if product_id:
        try:
            product_id = int(product_id)
            filtered_products = [p for p in products_list if p['id'] == product_id]
            if not filtered_products:
                return render_template('product_display.html', error="Product not found")
            products_list = filtered_products
        except ValueError:
            return render_template('product_display.html', error="Invalid product ID")
    
    return render_template('product_display.html', products=products_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
