from flask import Flask
from flasgger import Swagger
from .swagger_config import swagger_template, swagger_config
from .routes import register_routes
from flask_cors import CORS

def create_app():
    """
    Factory function to create and configure the Flask application.
    Loads Swagger documentation and registers API routes.
    """
    app = Flask(__name__)

    CORS(app)

    # Initialize Swagger with custom configuration
    Swagger(app, template=swagger_template, config=swagger_config)

    # Register application routes
    register_routes(app)

    return app
