#!/usr/bin/env python3
import requests
import csv

API_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_and_print_posts():
    """Fetches posts and prints the status code and titles."""
    response = requests.get(API_URL)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    """Fetches posts and saves them into a CSV file."""
    response = requests.get(API_URL)

    if response.status_code == 200:
        posts = response.json()
        data_to_save = [
            {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            for post in posts
        ]

        with open('posts.csv', mode='w', newline='', encoding='utf-8') as csv_file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(data_to_save)
