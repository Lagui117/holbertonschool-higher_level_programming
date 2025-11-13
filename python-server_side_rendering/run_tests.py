#!/usr/bin/python3
"""
Comprehensive test suite for the Server-Side Rendering project
Tests all tasks to ensure they work correctly
"""

import os
import sys
import json
import sqlite3

print("=" * 60)
print("Python Server-Side Rendering - Comprehensive Test Suite")
print("=" * 60)

# Test 1: Task 0 - Templating Function
print("\n[TEST 1] Testing Task 0 - Templating Function")
print("-" * 60)
try:
    from task_00_intro import generate_invitations
    
    # Test with valid data
    with open('template.txt', 'r') as file:
        template_content = file.read()
    
    attendees = [
        {"name": "Test User", "event_title": "Test Event", 
         "event_date": "2024-01-01", "event_location": "Test City"}
    ]
    
    generate_invitations(template_content, attendees)
    
    # Check if output file was created
    if os.path.exists('output_1.txt'):
        with open('output_1.txt', 'r') as f:
            content = f.read()
            if "Test User" in content and "Test Event" in content:
                print("✓ Task 0: PASSED - Template generation works correctly")
            else:
                print("✗ Task 0: FAILED - Output content incorrect")
    else:
        print("✗ Task 0: FAILED - Output file not created")
    
    # Test error handling
    generate_invitations("", [])  # Should print error message
    generate_invitations(None, [])  # Should print error message
    
except Exception as e:
    print(f"✗ Task 0: FAILED - {str(e)}")

# Test 2: Task 1 - Flask Application Structure
print("\n[TEST 2] Testing Task 1 - Flask Application Structure")
print("-" * 60)
try:
    from task_01_jinja import app
    
    # Check routes exist
    routes = [rule.rule for rule in app.url_map.iter_rules()]
    required_routes = ['/', '/about', '/contact']
    
    all_routes_exist = all(route in routes for route in required_routes)
    
    if all_routes_exist:
        print("✓ Task 1: PASSED - All routes exist")
    else:
        print(f"✗ Task 1: FAILED - Missing routes. Found: {routes}")
    
    # Check templates exist
    templates = ['index.html', 'about.html', 'contact.html', 
                 'header.html', 'footer.html']
    templates_dir = 'templates'
    
    all_templates_exist = all(
        os.path.exists(os.path.join(templates_dir, t)) for t in templates
    )
    
    if all_templates_exist:
        print("✓ Task 1: PASSED - All templates exist")
    else:
        print("✗ Task 1: FAILED - Some templates are missing")
        
except Exception as e:
    print(f"✗ Task 1: FAILED - {str(e)}")

# Test 3: Task 2 - Dynamic Content with JSON
print("\n[TEST 3] Testing Task 2 - Dynamic Content")
print("-" * 60)
try:
    from task_02_logic import app as app2
    
    # Check /items route exists
    routes = [rule.rule for rule in app2.url_map.iter_rules()]
    
    if '/items' in routes:
        print("✓ Task 2: PASSED - /items route exists")
    else:
        print("✗ Task 2: FAILED - /items route not found")
    
    # Check items.json exists
    if os.path.exists('items.json'):
        with open('items.json', 'r') as f:
            data = json.load(f)
            if 'items' in data:
                print(f"✓ Task 2: PASSED - items.json contains {len(data['items'])} items")
            else:
                print("✗ Task 2: FAILED - items.json structure incorrect")
    else:
        print("✗ Task 2: FAILED - items.json not found")
    
    # Check items.html template exists
    if os.path.exists('templates/items.html'):
        print("✓ Task 2: PASSED - items.html template exists")
    else:
        print("✗ Task 2: FAILED - items.html template not found")
        
except Exception as e:
    print(f"✗ Task 2: FAILED - {str(e)}")

# Test 4: Task 3 - JSON/CSV Data Sources
print("\n[TEST 4] Testing Task 3 - JSON/CSV Support")
print("-" * 60)
try:
    from task_03_files import read_json, read_csv
    
    # Test JSON reading
    json_data = read_json('products.json')
    if json_data and len(json_data) == 2:
        print(f"✓ Task 3: PASSED - JSON reading works ({len(json_data)} products)")
    else:
        print("✗ Task 3: FAILED - JSON reading failed")
    
    # Test CSV reading
    csv_data = read_csv('products.csv')
    if csv_data and len(csv_data) == 2:
        print(f"✓ Task 3: PASSED - CSV reading works ({len(csv_data)} products)")
    else:
        print("✗ Task 3: FAILED - CSV reading failed")
    
    # Check product_display.html exists
    if os.path.exists('templates/product_display.html'):
        print("✓ Task 3: PASSED - product_display.html template exists")
    else:
        print("✗ Task 3: FAILED - product_display.html template not found")
        
except Exception as e:
    print(f"✗ Task 3: FAILED - {str(e)}")

# Test 5: Task 4 - SQLite Support
print("\n[TEST 5] Testing Task 4 - SQLite Support")
print("-" * 60)
try:
    from task_04_db import read_sql
    
    # Check database exists
    if os.path.exists('products.db'):
        print("✓ Task 4: PASSED - products.db exists")
        
        # Test reading from database
        sql_data = read_sql('products.db')
        if sql_data and len(sql_data) == 2:
            print(f"✓ Task 4: PASSED - SQLite reading works ({len(sql_data)} products)")
            
            # Verify data structure
            if all('id' in p and 'name' in p and 'category' in p and 'price' in p 
                   for p in sql_data):
                print("✓ Task 4: PASSED - Data structure is correct")
            else:
                print("✗ Task 4: FAILED - Data structure incorrect")
        else:
            print("✗ Task 4: FAILED - SQLite reading failed")
    else:
        print("✗ Task 4: FAILED - products.db not found")
        print("  Run: python3 create_database.py")
        
except Exception as e:
    print(f"✗ Task 4: FAILED - {str(e)}")

# Summary
print("\n" + "=" * 60)
print("Test Summary")
print("=" * 60)
print("\nAll tasks have been tested!")
print("\nTo run the Flask applications:")
print("  Task 1: python3 task_01_jinja.py")
print("  Task 2: python3 task_02_logic.py")
print("  Task 3: python3 task_03_files.py")
print("  Task 4: python3 task_04_db.py")
print("\nThen visit http://localhost:5000 in your browser")
print("=" * 60)
