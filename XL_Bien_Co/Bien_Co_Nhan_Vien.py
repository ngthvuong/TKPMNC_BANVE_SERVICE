from flask import request, jsonify
from XL_Luu_Tru.NHAN_VIEN import NHAN_VIEN
from XL_Luu_Tru import db

from XL_Giao_Tiep.Nhan_Vien_Resource import Nhan_Vien_Resource

class Bien_Co_Nhan_Vien:
    def Quan_Ly(self):
        data = request.get_json()
        email = data.get('email')
        Vai_Tro = "Quan_Ly_Rap"
        nhan_vien = db.session.query(NHAN_VIEN).filter(NHAN_VIEN.Email == email, NHAN_VIEN.Vai_Tro == Vai_Tro).first()
        return jsonify(Nhan_Vien_Resource.resource(nhan_vien))

    def Nhan_Vien_Ban_Ve(self):
        data = request.get_json()
        email = data.get('email')
        Vai_Tro = "Nhan_Vien_Ban_Ve"
        nhan_vien = db.session.query(NHAN_VIEN).filter(NHAN_VIEN.Email == email, NHAN_VIEN.Vai_Tro == Vai_Tro).first()
        return jsonify(Nhan_Vien_Resource.resource(nhan_vien))
