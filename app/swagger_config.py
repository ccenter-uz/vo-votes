"""
Configuration for Flasgger (Swagger UI)
Used to enable and customize API documentation
"""

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Call Center Voting API",
        "description": "API that caches each poll ID on demand and refreshes it every 5 seconds.",
        "version": "1.0.0"
    },
    "basePath": "/",
    "schemes": ["https"]
}

swagger_config = {
    "headers": [],
    "specs": [{
        "endpoint": 'apispec_1',
        "route": '/apispec_1.json',
        "rule_filter": lambda rule: True,  
        "model_filter": lambda tag: True   
    }],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/"
}
