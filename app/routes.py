from flask import jsonify, request
from .services.fetcher import fetch_votes
from .core.cache import cache, update_queue

def register_routes(app):
    """
    Register all Flask routes to the application.
    """

    @app.route("/", methods=["GET"])
    def get_by_id():
        """
        Get cached or fresh voting results by ID
        ---
        tags:
          - Votes
        parameters:
          - name: id
            in: query
            type: string
            required: true
            description: ID provided by the call center 
        responses:
          200:
            description: Vote results
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
                    example: "1245"
          400:
            description: Missing or invalid ID
        """
        poll_id = request.args.get("id")
        if not poll_id:
            return jsonify({"error": "Missing required parameter: id"}), 400

        if poll_id in cache:
            print(f"[INFO] Cache HIT: {poll_id}")
            return jsonify(cache[poll_id])

        try:
            print(f"[INFO] Cache MISS: {poll_id}. Fetching and enabling auto-refresh.")
            result = fetch_votes(poll_id)
            cache[poll_id] = result
            update_queue.add(poll_id)
            return jsonify(result)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
