from flask import Blueprint
from XL_Bien_Co.Bien_Co_Nhan_Vien import Bien_Co_Nhan_Vien
from XL_Bien_Co.Bien_Co_Xuat_Chieu import Bien_Co_Xuat_Chieu

Ban_Ve_BP = Blueprint("banve", __name__, url_prefix="/banve")

XL_Bien_Co_Nhan_Vien = Bien_Co_Nhan_Vien()
XL_Bien_Co_Xuat_Chieu = Bien_Co_Xuat_Chieu()


@Ban_Ve_BP.route("/nhanvien", methods=['POST'])
def Nhan_Vien_Ban_Ve():
    return XL_Bien_Co_Nhan_Vien.Nhan_Vien_Ban_Ve()

@Ban_Ve_BP.route("/xuatchieu", methods=['GET'])
def Lay_Danh_Sach_Chua_Chieu():
    return XL_Bien_Co_Xuat_Chieu.Lay_Danh_Sach_Chua_Chieu()