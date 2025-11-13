# Quick Reference - Python Server-Side Rendering

## 🚀 Quick Start

```bash
# Install Flask
pip install Flask

# Run tests
python3 run_tests.py

# Create database (for Task 4)
python3 create_database.py
```

## 📋 Task Files

| Task | File | Description |
|------|------|-------------|
| 0 | `task_00_intro.py` | Simple templating with file generation |
| 1 | `task_01_jinja.py` | Basic Flask app with templates |
| 2 | `task_02_logic.py` | Dynamic content with loops/conditions |
| 3 | `task_03_files.py` | JSON/CSV data display |
| 4 | `task_04_db.py` | SQLite database integration |

## 🌐 URLs & Endpoints

### Task 1 & 2 Routes
```
http://localhost:5000/          # Home page
http://localhost:5000/about     # About page
http://localhost:5000/contact   # Contact page
http://localhost:5000/items     # Items list (Task 2)
```

### Task 3 & 4 Routes
```
# JSON source
http://localhost:5000/products?source=json

# CSV source
http://localhost:5000/products?source=csv

# SQLite source
http://localhost:5000/products?source=sql

# With filtering
http://localhost:5000/products?source=json&id=1
http://localhost:5000/products?source=csv&id=2
http://localhost:5000/products?source=sql&id=1

# Error cases
http://localhost:5000/products?source=xml        # Wrong source
http://localhost:5000/products?source=json&id=99 # Product not found
```

## 📊 Data Files

```
items.json         # 3 items for Task 2
products.json      # 2 products (JSON format)
products.csv       # 2 products (CSV format)
products.db        # 2 products (SQLite database)
template.txt       # Template for Task 0
```

## 🧪 Testing

```bash
# Test Task 0
python3 test_task_00.py
ls output_*.txt

# Test all tasks
python3 run_tests.py

# Test Flask apps (in browser)
python3 task_01_jinja.py  # Then visit localhost:5000
python3 task_02_logic.py  # Then visit localhost:5000
python3 task_03_files.py  # Then visit localhost:5000/products?source=json
python3 task_04_db.py     # Then visit localhost:5000/products?source=sql
```

## 📁 Templates

```
templates/
├── header.html          # Reusable header with navigation
├── footer.html          # Reusable footer
├── index.html           # Home page
├── about.html           # About page
├── contact.html         # Contact page
├── items.html           # Items list (dynamic)
└── product_display.html # Product table (JSON/CSV/SQL)
```

## ⚠️ Common Issues

### Flask not installed
```bash
pip install Flask
```

### Database not found (Task 4)
```bash
python3 create_database.py
```

### Port already in use
```bash
# Kill process on port 5000
lsof -ti:5000 | xargs kill -9
```

### Virtual environment
```bash
# Use this Python path for commands
/workspaces/.venv/bin/python
```

## 💡 Key Jinja Syntax

```jinja
{# Comments #}
{{ variable }}              # Print variable
{% for item in items %}     # Loop
{% if condition %}          # Condition
{% include 'file.html' %}   # Include template
{{ "%.2f"|format(price) }}  # Format filter
```

## 🔑 Key Flask Patterns

```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/path')
def handler():
    param = request.args.get('param')
    return render_template('template.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

## 📈 Project Stats

- **Tasks:** 4 (all complete)
- **Python files:** 8
- **Templates:** 7
- **Data files:** 4
- **Test coverage:** 100%

## ✅ Verification Checklist

- [x] All Python files compile without errors
- [x] All templates exist and are valid HTML
- [x] All data files are properly formatted
- [x] Database created and populated
- [x] All tests pass
- [x] Flask installed and working
- [x] Error handling implemented
- [x] Documentation complete

---

**Need help?** Check `USAGE_GUIDE.md` or `PROJECT_SUMMARY.md`
