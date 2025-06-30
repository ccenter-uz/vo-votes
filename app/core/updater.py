import time
from app.services.fetcher import fetch_votes
from app.core.cache import cache, update_queue
import os
from dotenv import load_dotenv

load_dotenv()

# Read update interval (in seconds) from .env file, default is 5
UPDATE_INTERVAL = int(os.getenv("UPDATE_INTERVAL", 5))

def background_refresher():
    """
    Background job that continuously refreshes cached data
    for all IDs in the update_queue every UPDATE_INTERVAL seconds.
    """
    while True:
        for poll_id in list(update_queue):
            try:
                result = fetch_votes(poll_id)
                cache[poll_id] = result
                print(f"[INFO] Cache refreshed: {poll_id}")
            except Exception as e:
                print(f"[ERROR] Failed to update {poll_id}: {e}")
        time.sleep(UPDATE_INTERVAL)
