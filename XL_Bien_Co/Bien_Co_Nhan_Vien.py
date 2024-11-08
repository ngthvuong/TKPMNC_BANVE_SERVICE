from flask import request, jsonify
from XL_Luu_Tru.NHAN_VIEN import NHAN_VIEN
from XL_Luu_Tru import db

from XL_Giao_Tiep.Giao_Tiep_Nhan_Vien import Giao_Tiep_Nhan_Vien

class Bien_Co_Nhan_Vien:
    def Quan_Ly(self):
        Yeu_Cau = request.get_json()
        Email = Yeu_Cau.get('Email')
        Vai_Tro = "Quan_Ly_Rap"
        nhan_vien = db.session.query(NHAN_VIEN).filter(NHAN_VIEN.Email == Email, NHAN_VIEN.Vai_Tro == Vai_Tro).first()
        return jsonify(Giao_Tiep_Nhan_Vien.Doi_Tuong(nhan_vien))

    def Nhan_Vien_Ban_Ve(self):
        Yeu_Cau = request.get_json()
        Email = Yeu_Cau.get('Email')
        Vai_Tro = "Nhan_Vien_Ban_Ve"
        nhan_vien = db.session.query(NHAN_VIEN).filter(NHAN_VIEN.Email == Email, NHAN_VIEN.Vai_Tro == Vai_Tro).first()
        return jsonify(Giao_Tiep_Nhan_Vien.Doi_Tuong(nhan_vien))
