#!/usr/bin/env python3
"""
Task 02 - Consume and process data from an API using Python (requests).

- fetch_and_print_posts(): GET all posts, print Status Code and each title.
- fetch_and_save_posts(): GET all posts, save id/title/body to posts.csv.
"""
from typing import List, Dict
import csv
import sys

try:
    import requests
except Exception as e:
    print(
        "Missing dependency 'requests'. Run: pip install requests",
        file=sys.stderr,
    )
    raise e

API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts() -> None:
    """Fetch posts and print status code then all titles."""
    resp = requests.get(API_URL, timeout=10)
    print(f"Status Code: {resp.status_code}")
    if resp.ok:
        try:
            data = resp.json()
        except ValueError:
            print("Error: Response is not JSON")
            return
        for post in data:
            title = post.get("title")
            if title is not None:
                print(title)


def fetch_and_save_posts(filename: str = "posts.csv") -> None:
    """Fetch posts and save id/title/body to CSV."""
    resp = requests.get(API_URL, timeout=10)
    if not resp.ok:
        print(
            f"Error: GET {API_URL} -> {resp.status_code}",
            file=sys.stderr,
        )
        return

    try:
        data = resp.json()
    except ValueError:
        print("Error: Response is not JSON", file=sys.stderr)
        return

    rows: List[Dict[str, str]] = []
    for post in data:
        rows.append(
            {
                "id": str(post.get("id")),
                "title": str(post.get("title")),
                "body": str(post.get("body")),
            }
        )

    fieldnames = ["id", "title", "body"]
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
