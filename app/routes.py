from flask import jsonify
from .services.fetcher import fetch_votes
from .core.cache import cache, update_queue

def register_routes(app):
    """
    Register all Flask routes to the application.
    """

    @app.route("/<id>", methods=["GET"])
    def get_by_id(id):
        """
        Get cached or fresh voting results by ID.
        ---
        tags:
          - Votes
        parameters:
          - name: id
            in: path
            type: string
            required: true
            description: ID provided by the call center
        responses:
          200:
            description: List of vote results
            schema:
              type: array
              items:
                type: object
                properties:
                  number:
                    type: string
                    example: "1"
                  votes:
                    type: string
                    example: "1200"
          500:
            description: Failed to fetch or process data
        """
        # Return from cache if available
        if id in cache:
            print(f"[INFO] Cache HIT: {id}")
            return jsonify(cache[id])
        
        # Otherwise, fetch live and store in cache
        try:
            print(f"[INFO] Cache MISS: {id}. Fetching and enabling auto-refresh.")
            result = fetch_votes(id)
            cache[id] = result
            update_queue.add(id)
            return jsonify(result)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
