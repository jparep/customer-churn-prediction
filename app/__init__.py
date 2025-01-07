from flask import Flask

def create_app(config_object=None):
    """
    Factory function to create and configure the Flask application.

    Args:
        config_object: The configuration object or file to load app settings (default: None).

    Returns:
        Flask app instance.
    """
    app = Flask(__name__)

    # Load configuration if provided
    if config_object:
        app.config.from_object(config_object)

    # Register routes
    from .routes import api
    app.register_blueprint(api, url_prefix='/api')

    # Optional: Add other initializations like extensions or middleware
    # Example: Initialize database, logging, etc.

    return app
