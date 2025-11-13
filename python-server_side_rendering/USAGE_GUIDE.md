# Python Server-Side Rendering - Usage Guide

## Overview
This project implements server-side rendering using Python Flask and Jinja templating engine. It demonstrates reading data from multiple sources (JSON, CSV, SQLite) and rendering dynamic HTML pages.

## Prerequisites
```bash
pip install Flask
```

## Tasks Overview

### Task 0: Simple Templating Program
**File:** `task_00_intro.py`

Generates personalized invitation files from a template.

**Usage:**
```python
from task_00_intro import generate_invitations

with open('template.txt', 'r') as file:
    template_content = file.read()

attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

generate_invitations(template_content, attendees)
```

**Output:** Creates `output_1.txt`, `output_2.txt`, `output_3.txt` with personalized invitations.

---

### Task 1: Basic HTML Template in Flask
**File:** `task_01_jinja.py`

Basic Flask application with reusable header and footer templates.

**Usage:**
```bash
python3 task_01_jinja.py
```

**Access:**
- Home: http://localhost:5000/
- About: http://localhost:5000/about
- Contact: http://localhost:5000/contact

**Features:**
- Reusable header with navigation
- Reusable footer
- Multiple pages with consistent layout

---

### Task 2: Dynamic Templates with Loops and Conditions
**File:** `task_02_logic.py`

Displays items from JSON file using Jinja loops and conditions.

**Usage:**
```bash
python3 task_02_logic.py
```

**Access:**
- Items page: http://localhost:5000/items

**Features:**
- Reads from `items.json`
- Displays items in unordered list
- Shows "No items found" when list is empty

**Test with empty list:**
Edit `items.json`:
```json
{
    "items": []
}
```

---

### Task 3: Display Data from JSON/CSV Files
**File:** `task_03_files.py`

Displays product data from JSON or CSV files with optional filtering.

**Usage:**
```bash
python3 task_03_files.py
```

**Access:**
- All JSON products: http://localhost:5000/products?source=json
- All CSV products: http://localhost:5000/products?source=csv
- Specific product (JSON): http://localhost:5000/products?source=json&id=1
- Specific product (CSV): http://localhost:5000/products?source=csv&id=2
- Invalid source: http://localhost:5000/products?source=xml (returns "Wrong source" error)
- Invalid ID: http://localhost:5000/products?source=json&id=999 (returns "Product not found")

**Features:**
- Reads from `products.json` or `products.csv`
- Filters by product ID when provided
- Error handling for invalid sources and missing products
- Displays data in HTML table format

---

### Task 4: Display Data from SQLite Database
**File:** `task_04_db.py`

Extends Task 3 to include SQLite database as a data source.

**Setup Database:**
```bash
python3 create_database.py
```

**Usage:**
```bash
python3 task_04_db.py
```

**Access:**
- All products (JSON): http://localhost:5000/products?source=json
- All products (CSV): http://localhost:5000/products?source=csv
- All products (SQLite): http://localhost:5000/products?source=sql
- Specific product (SQLite): http://localhost:5000/products?source=sql&id=1

**Features:**
- Reads from `products.db` SQLite database
- Same template and filtering as Task 3
- Complete error handling

---

## Data Files

### products.json
```json
[
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 799.99},
    {"id": 2, "name": "Coffee Mug", "category": "Home Goods", "price": 15.99}
]
```

### products.csv
```csv
id,name,category,price
1,Laptop,Electronics,799.99
2,Coffee Mug,Home Goods,15.99
```

### products.db (SQLite)
Table: Products
- id (INTEGER PRIMARY KEY)
- name (TEXT)
- category (TEXT)
- price (REAL)

---

## Templates Structure

```
templates/
├── header.html          # Reusable header with navigation
├── footer.html          # Reusable footer
├── index.html           # Home page
├── about.html           # About page
├── contact.html         # Contact page
├── items.html           # Items list with loops/conditions
└── product_display.html # Product table display
```

---

## Testing

### Test Task 0:
```bash
python3 test_task_00.py
cat output_1.txt
cat output_2.txt
cat output_3.txt
```

### Test Task 1:
```bash
python3 task_01_jinja.py
# Open browser to http://localhost:5000
```

### Test Task 2:
```bash
python3 task_02_logic.py
# Open browser to http://localhost:5000/items
```

### Test Task 3:
```bash
python3 task_03_files.py
# Test various URLs:
# http://localhost:5000/products?source=json
# http://localhost:5000/products?source=csv
# http://localhost:5000/products?source=json&id=1
# http://localhost:5000/products?source=xml (error test)
```

### Test Task 4:
```bash
python3 create_database.py  # Create database first
python3 task_04_db.py
# Test URL:
# http://localhost:5000/products?source=sql
# http://localhost:5000/products?source=sql&id=2
```

---

## Error Handling

### Task 0 Errors:
- Empty template: "Template is empty, no output files generated."
- Empty attendees: "No data provided, no output files generated."
- Invalid type: "Error: Template must be a string" or "Error: Attendees must be a list of dictionaries"
- Missing data: Replaced with "N/A"

### Task 3 & 4 Errors:
- Invalid source: "Wrong source"
- Product not found: "Product not found"
- File/DB read error: "Error reading data"

---

## Project Structure
```
python-server_side_rendering/
├── task_00_intro.py           # Templating function
├── template.txt                # Template for task 0
├── task_01_jinja.py           # Basic Flask app
├── task_02_logic.py           # Dynamic content
├── task_03_files.py           # JSON/CSV support
├── task_04_db.py              # SQLite support
├── create_database.py         # Database setup script
├── items.json                 # Items data
├── products.json              # Products (JSON format)
├── products.csv               # Products (CSV format)
├── products.db                # Products (SQLite database)
├── test_task_00.py            # Test script for task 0
├── README.md                  # Project documentation
└── templates/                 # HTML templates
    ├── header.html
    ├── footer.html
    ├── index.html
    ├── about.html
    ├── contact.html
    ├── items.html
    └── product_display.html
```

## Key Concepts

### Server-Side Rendering (SSR)
- HTML is generated on the server
- Complete pages sent to client
- Better for SEO
- Faster initial page load

### Jinja Templating
- Template inheritance with `{% include %}`
- Loops with `{% for %}`
- Conditions with `{% if %}`
- Variable interpolation with `{{ variable }}`

### Data Sources
- JSON: Structured data format
- CSV: Comma-separated values
- SQLite: Relational database

## Tips
1. Always run Flask apps with `debug=True` during development
2. Use port 5000 for consistency
3. Test edge cases (empty data, invalid IDs, missing files)
4. Validate input types before processing
5. Provide meaningful error messages
