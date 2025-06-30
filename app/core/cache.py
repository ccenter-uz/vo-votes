"""
Simple in-memory cache and dynamic update queue
"""

# Stores cached results in memory (ID -> list of {number, votes})
cache = {}

# Set of IDs that should be refreshed periodically in the background
update_queue = set()
