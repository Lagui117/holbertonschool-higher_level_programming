#!/usr/bin/env python3
"""
Task 02 - Consume and process data from an API using Python (requests).

Functions:
- fetch_and_print_posts(): GET all posts, print Status Code and each title.
- fetch_and_save_posts(): GET all posts, save id/title/body to posts.csv.
"""
import requests
import csv


API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetch posts and print status code and all titles."""
    try:
        response = requests.get(API_URL)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            posts = response.json()
            for post in posts:
                print(post.get("title"))
        else:
            print("Fetch failed")
    except Exception:
        print("Fetch failed")


def fetch_and_save_posts():
    """Fetch posts and save id, title, body to posts.csv."""
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            posts = response.json()
            with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
                fieldnames = ["id", "title", "body"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for post in posts:
                    writer.writerow({
                        "id": post.get("id"),
                        "title": post.get("title"),
                        "body": post.get("body")
                    })
        else:
            print("Fetch failed")
    except Exception:
        print("Fetch failed")
