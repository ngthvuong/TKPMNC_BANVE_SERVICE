from flask import jsonify, request
from XL_Luu_Tru.XUAT_CHIEU import XUAT_CHIEU

from XL_Luu_Tru.PHIM import PHIM
from XL_Luu_Tru.CA import CA
from XL_Luu_Tru.VE import VE
from XL_Luu_Tru.PHONG import PHONG
from XL_Luu_Tru.LOAI_PHONG import LOAI_PHONG
from XL_Luu_Tru.RAP import RAP

from XL_Luu_Tru import db
from sqlalchemy.orm import joinedload
from datetime import date, datetime, timedelta

from XL_Giao_Tiep.Giao_Tiep_Xuat_Chieu import Giao_Tiep_Xuat_Chieu

class Bien_Co_Xuat_Chieu:
    def Lay_Danh_Sach_Chua_Chieu(self):
        Xuat_Chieus = (
            db.session.query(XUAT_CHIEU)
            .options(
                joinedload(XUAT_CHIEU.Phim),
                joinedload(XUAT_CHIEU.Ca),
                joinedload(XUAT_CHIEU.Phong).joinedload(PHONG.Loai_Phong),
                joinedload(XUAT_CHIEU.Phong).joinedload(PHONG.Rap),
                # joinedload(XUAT_CHIEU.Ves).joinedload(VE.Ghe),
            )
            .filter(
                XUAT_CHIEU.Ngay_Chieu >= date.today()
            )
            .all()
        )
        return jsonify({"data" : Giao_Tiep_Xuat_Chieu.Danh_Sach(Xuat_Chieus)})
    
    def Lay_Danh_Sach_Chua_Chieu_Theo_Quan_Ly(self):
        Xuat_Chieus = (
            db.session.query(XUAT_CHIEU)
            .options(
                joinedload(XUAT_CHIEU.Phim),
                joinedload(XUAT_CHIEU.Ca),
                joinedload(XUAT_CHIEU.Phong).joinedload(PHONG.Loai_Phong),
                joinedload(XUAT_CHIEU.Phong).joinedload(PHONG.Rap),
                # joinedload(XUAT_CHIEU.Ves).joinedload(VE.Ghe),
            )
            .filter(
                XUAT_CHIEU.Phong.has(PHONG.Rap_ID.in_([1,2])),
                XUAT_CHIEU.Ngay_Chieu >= date.today()
            )
            .all()
        )
        return jsonify({"data" : Giao_Tiep_Xuat_Chieu.Danh_Sach(Xuat_Chieus)})    
    def Lay_Xuat_Chieu(self):
        return jsonify({"success" : True})
    
    def Them_Xuat_Chieu(self):
        return jsonify({"success" : True})
    
    def Sua_Xuat_Chieu(self):
        return jsonify({"success" : True})
    
    def Xoa_Xuat_Chieu(self):
        return jsonify({"success" : True})