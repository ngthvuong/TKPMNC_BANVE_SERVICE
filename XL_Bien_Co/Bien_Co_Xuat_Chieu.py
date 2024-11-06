from flask import jsonify, request
from XL_Luu_Tru.XUAT_CHIEU import XUAT_CHIEU

from XL_Luu_Tru.PHIM import PHIM
from XL_Luu_Tru.CA import CA
from XL_Luu_Tru.VE import VE
from XL_Luu_Tru.PHONG import PHONG
from XL_Luu_Tru.LOAI_PHONG import LOAI_PHONG
from XL_Luu_Tru.RAP import RAP

from XL_Luu_Tru import db

class Bien_Co_Xuat_Chieu:
    def Lay_Danh_Sach_Chua_Chieu(self):
        return jsonify({"success" : True})
    
    def Lay_Danh_Sach_Chua_Chieu_Theo_Quan_Ly(self):
        return jsonify({"success" : True})
    
    def Lay_Xuat_Chieu(self):
        return jsonify({"success" : True})
    
    def Them_Xuat_Chieu(self):
        return jsonify({"success" : True})
    
    def Sua_Xuat_Chieu(self):
        return jsonify({"success" : True})
    
    def Xoa_Xuat_Chieu(self):
        return jsonify({"success" : True})