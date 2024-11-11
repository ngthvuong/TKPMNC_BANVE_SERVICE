from flask import jsonify
from XL_Luu_Tru.PHIM import PHIM
from XL_Luu_Tru import db

from XL_Giao_Tiep.Giao_Tiep_Phim import Giao_Tiep_Phim

class Bien_Co_Phim:
    def Lay_Danh_Sach_Phim(self):
        Phims = (
            db.session.query(PHIM).all()
        )
        return jsonify(Giao_Tiep_Phim.Danh_Sach(Phims))