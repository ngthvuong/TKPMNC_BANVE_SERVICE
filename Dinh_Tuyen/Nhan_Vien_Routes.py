from flask import Blueprint
from XL_Bien_Co.Nhan_Vien_Controller import Nhan_Vien_Controller

nhan_vien_bp = Blueprint("nhanvien", __name__, url_prefix="/nhanvien")
Xu_Ly_Bien_Co = Nhan_Vien_Controller()

@nhan_vien_bp.route("/", methods=['GET'])
def get():
    return Xu_Ly_Bien_Co.get()