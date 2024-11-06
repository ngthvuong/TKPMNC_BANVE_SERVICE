from flask import Blueprint
from XL_Bien_Co.Bien_Co_Nhan_Vien import Bien_Co_Nhan_Vien

XL_Bien_Co = Bien_Co_Nhan_Vien

Quan_Ly_BP = Blueprint("quanly", __name__, url_prefix="/quanly")

@Quan_Ly_BP.route("/nhanvien", methods=['POST'])
def Quan_Ly():
    return XL_Bien_Co.Quan_Ly()