# app/cache.py

import redis
import json
from typing import Optional

# Initialize Redis client
try:
    r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)
except redis.exceptions.ConnectionError:
    r = None
    print("Redis is not available.")

# Function to get list of books from cache
def get_books_from_cache() -> Optional[list[dict]]:
    try:
        if r is None:
            raise redis.exceptions.ConnectionError("Redis not initialized")
        cached_books = r.get("books")
        if cached_books:
            return json.loads(cached_books)
    except redis.exceptions.ConnectionError:
        print("⚠️ Redis is down or unavailable.")
    return None

# Function to store list of books to cache
def set_books_to_cache(data: list[dict]) -> None:
    try:
        if r is None:
            raise redis.exceptions.ConnectionError("Redis not initialized")
        r.set("books", json.dumps(data), ex=60)  # 60-second TTL
    except redis.exceptions.ConnectionError:
        print("⚠️ Could not connect to Redis to set cache.")
