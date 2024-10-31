from .task_routes import task_routes
from .user_routes import user_routes
from .version_routes import version_routes
from .swagger_routes import swagger_routes

def register_blueprints(app):
    app.register_blueprint(task_routes)
    app.register_blueprint(user_routes)
    app.register_blueprint(version_routes)
    app.register_blueprint(swagger_routes)