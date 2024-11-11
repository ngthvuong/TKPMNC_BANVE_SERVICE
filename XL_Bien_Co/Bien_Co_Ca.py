from flask import jsonify

from XL_Luu_Tru.CA import CA
from XL_Luu_Tru import db

from XL_Giao_Tiep.Giao_Tiep_Ca import Giao_Tiep_Ca

class Bien_Co_Ca:
    def Lay_Danh_Sach_Ca(self):
        Cas = (
            db.session.query(CA).all()
        )
        return jsonify(Giao_Tiep_Ca.Danh_Sach(Cas))