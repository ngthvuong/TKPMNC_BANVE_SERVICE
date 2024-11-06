from Dinh_Tuyen.Ban_Ve import Ban_Ve_BP
from Dinh_Tuyen.Quan_Ly import Quan_Ly_BP
from Dinh_Tuyen.Xac_Thuc_Ung_Dung import Xac_Thuc_BP


from flask import Blueprint

root_bp = Blueprint("root", __name__, url_prefix="/")
root_bp.register_blueprint(Xac_Thuc_BP) # Xác Thực Ứng Dụng
root_bp.register_blueprint(Ban_Ve_BP) # Ứng dụng Bán Vé
root_bp.register_blueprint(Quan_Ly_BP) # Ứng dụng Quản Lý

def init_routes(app):
    app.register_blueprint(root_bp)