from flask import request, jsonify
from XL_Luu_Tru.NHAN_VIEN import NHAN_VIEN
from XL_Luu_Tru import db

from XL_Giao_Tiep.Nhan_Vien_Resource import Nhan_Vien_Resource

class Nhan_Vien_Controller:
    def get(self):
        data = request.get_json()
        email = data.get('email')
        nhan_vien = db.session.query(NHAN_VIEN).filter(NHAN_VIEN.Email == email).first()
        return jsonify({"data": Nhan_Vien_Resource.resource(nhan_vien)})
