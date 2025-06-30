from flask import Flask
from flasgger import Swagger
from .swagger_config import swagger_template, swagger_config
from .routes import register_routes

def create_app():
    """
    Factory function to create and configure the Flask application.
    Loads Swagger documentation and registers API routes.
    """
    app = Flask(__name__)

    # Initialize Swagger with custom configuration
    Swagger(app, template=swagger_template, config=swagger_config)

    # Register application routes
    register_routes(app)

    return app
