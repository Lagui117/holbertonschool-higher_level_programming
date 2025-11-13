#!/usr/bin/python3
"""Flask application to display data from JSON or CSV files."""
from flask import Flask, render_template, request
import json
import csv

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


@app.route('/products')
def products():
    """Display products from JSON or CSV file based on source parameter."""
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    # Validate source parameter
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")
    
    # Read data based on source
    if source == 'json':
        products_list = read_json()
    else:  # source == 'csv'
        products_list = read_csv()
    
    # Handle file reading errors
    if products_list is None:
        return render_template('product_display.html', error="Error reading file")
    
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
