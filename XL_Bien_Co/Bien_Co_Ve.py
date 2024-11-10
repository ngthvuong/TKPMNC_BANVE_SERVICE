from flask import jsonify, request
from XL_Luu_Tru.VE import VE
from XL_Luu_Tru.XUAT_CHIEU import XUAT_CHIEU
from XL_Luu_Tru.PHONG import PHONG
from XL_Luu_Tru.GHE import GHE

from XL_Luu_Tru import db
from sqlalchemy.orm import joinedload

from XL_Giao_Tiep.Giao_Tiep_Ve import Giao_Tiep_Ve

class Bien_Co_Ve:
    def Tao_Ve(self):
        Yeu_Cau = request.get_json()
        Ghe_ID = Yeu_Cau.get('Ghe_ID')
        Xuat_Chieu_ID = Yeu_Cau.get('Xuat_Chieu_ID')
        
        Xuat_Chieu = (
            db.session.query(XUAT_CHIEU)
            .options(
                joinedload(XUAT_CHIEU.Phong).joinedload(PHONG.Ghes),
            )
            .filter(
                XUAT_CHIEU.ID == Xuat_Chieu_ID,
                PHONG.Ghes.any(GHE.ID == Ghe_ID)
            )
            .first()
        )
        if not Xuat_Chieu:
            return jsonify({"error": "Xuất chiếu hoặc ghế không phù hợp!" })
        
        Ghe_Co_Ve = (
            db.session.query(VE)
            .filter(
                VE.Xuat_Chieu_ID == Xuat_Chieu_ID,
                VE.Ghe_ID == Ghe_ID
            )
            .first()
        )
        if Ghe_Co_Ve:
            return jsonify({"error": "Ghế đã được đặt!" })
        
        Ve_Moi = VE(Ghe_ID=Ghe_ID, Xuat_Chieu_ID=Xuat_Chieu_ID, Gia=Xuat_Chieu.Don_Gia)
        db.session.add(Ve_Moi)
        db.session.commit()

        return jsonify(Giao_Tiep_Ve.Doi_Tuong(Ve_Moi))
    
    def Lay_Ve_Theo_Xuat_Chieu(self):
        # Thêm Vé
        return jsonify({"success": True })
    
    def Thong_Ke_So_Ve_Ban():
        # Tháng
        # Năm
        return jsonify({"success": True })
        