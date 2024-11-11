from flask import Blueprint
from XL_Bien_Co.Bien_Co_Nhan_Vien import Bien_Co_Nhan_Vien
from XL_Bien_Co.Bien_Co_Xuat_Chieu import Bien_Co_Xuat_Chieu
from XL_Bien_Co.Bien_Co_Rap import Bien_Co_Rap
from XL_Bien_Co.Bien_Co_Ca import Bien_Co_Ca
from XL_Bien_Co.Bien_Co_Phim import Bien_Co_Phim


XL_Bien_Co_Nhan_Vien = Bien_Co_Nhan_Vien()
XL_Bien_Co_Xuat_Chieu = Bien_Co_Xuat_Chieu()
XL_Bien_Co_Rap = Bien_Co_Rap()
XL_Bien_Co_Ca = Bien_Co_Ca()
XL_Bien_Co_Phim = Bien_Co_Phim()


Quan_Ly_BP = Blueprint("quanly", __name__, url_prefix="/quanly")

@Quan_Ly_BP.route("/nhanvien", methods=['POST'])
def Quan_Ly():
    return XL_Bien_Co_Nhan_Vien.Quan_Ly()

@Quan_Ly_BP.route("/xuatchieu/danhsachchuachieu", methods=['GET'])
def Lay_Danh_Sach_Chua_Chieu():
    return XL_Bien_Co_Xuat_Chieu.Lay_Danh_Sach_Chua_Chieu()

@Quan_Ly_BP.route("/xuatchieu/danhsachchuachieu/<int:Quan_Ly_ID>", methods=['GET'])
def Lay_Danh_Sach_Chua_Chieu_Theo_Quan_Ly(Quan_Ly_ID):
    return XL_Bien_Co_Xuat_Chieu.Lay_Danh_Sach_Chua_Chieu_Theo_Quan_Ly(Quan_Ly_ID)

@Quan_Ly_BP.route("/xuatchieu", methods=['GET'])
def Lay_Xuat_Chieu():
    return XL_Bien_Co_Xuat_Chieu.Lay_Xuat_Chieu()

@Quan_Ly_BP.route("/rap/danhsachquanly/<int:Quan_Ly_ID>", methods=['GET'])
def Lay_Danh_Sach_Rap_Theo_Quan_Ly(Quan_Ly_ID):
    return XL_Bien_Co_Rap.Lay_Danh_Sach_Rap_Theo_Quan_Ly(Quan_Ly_ID)

@Quan_Ly_BP.route("/phim/danhsach", methods=['GET'])
def Lay_Danh_Sach_Phim():
    return XL_Bien_Co_Phim.Lay_Danh_Sach_Phim()

@Quan_Ly_BP.route("/ca/danhsach", methods=['GET'])
def Lay_Danh_Sach_Ca():
    return XL_Bien_Co_Ca.Lay_Danh_Sach_Ca()

