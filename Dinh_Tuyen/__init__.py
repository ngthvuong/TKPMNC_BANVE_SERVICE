from .Nhan_Vien_Routes import nhan_vien_bp

def init_routes(app):
    app.register_blueprint(nhan_vien_bp)


