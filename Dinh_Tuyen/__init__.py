from .user_routes import user_bp

def init_routes(app):
    app.register_blueprint(user_bp)


