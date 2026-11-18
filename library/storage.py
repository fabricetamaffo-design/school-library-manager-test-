"""Save and load the library catalogue as JSON."""

import json

from .models import Book


def save_books(books, path):
    f = open(path, "w", encoding="utf-8")
    json.dump([b.__dict__ for b in books], f, indent=2)


def load_books(path):
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except:
        return []
    return [Book(**item) for item in data]
