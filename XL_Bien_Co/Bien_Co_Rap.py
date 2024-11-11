from flask import jsonify

from XL_Luu_Tru.PHONG import PHONG
from XL_Luu_Tru.RAP import RAP

from XL_Luu_Tru import db
from sqlalchemy.orm import joinedload

from XL_Giao_Tiep.Giao_Tiep_Rap import Giao_Tiep_Rap

class Bien_Co_Rap:
    def Lay_Danh_Sach_Rap_Theo_Quan_Ly(self, Quan_Ly_ID):
        Raps = (
            db.session.query(RAP)
            .options(
                joinedload(RAP.Phongs)
            )
            .filter(
                RAP.Quan_Ly_ID == Quan_Ly_ID
            )
            .all()
        )
        return jsonify(Giao_Tiep_Rap.Danh_Sach(Raps))