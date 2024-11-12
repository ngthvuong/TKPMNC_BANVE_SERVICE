from flask import jsonify, request
from XL_Luu_Tru.VE import VE
from XL_Luu_Tru.XUAT_CHIEU import XUAT_CHIEU
from XL_Luu_Tru.CA import CA
from XL_Luu_Tru.PHONG import PHONG
from XL_Luu_Tru.GHE import GHE

from XL_Nghiep_Vu.Nghiep_Vu_Thong_Ke_Ve import Nghiep_Vu_Thong_Ke_Ve

from XL_Luu_Tru import db
from sqlalchemy.orm import joinedload
from sqlalchemy import func, extract



from XL_Giao_Tiep.Giao_Tiep_Ve import Giao_Tiep_Ve
from XL_Giao_Tiep.Giao_Tiep_Ve_Theo_Ca import Giao_Tiep_Ve_Theo_Ca


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
    
    
    def Thong_Ke_So_Ve_Ban_Theo_Thang(self, Thang, Nam):

        Danh_Sach_Tong_Ve_Theo_Ca = (
            db.session.query(
                CA.ID.label("ID"),
                CA.Bat_Dau.label("Bat_Dau"),
                CA.Ket_Thuc.label("Ket_Thuc"),
                CA.Ten.label("Ten"),
                func.count(VE.ID).label("So_Luong_Ve"),
            )
            .select_from(CA)
            .outerjoin(XUAT_CHIEU, XUAT_CHIEU.Ca_ID == CA.ID)
            .outerjoin(VE, VE.Xuat_Chieu_ID == XUAT_CHIEU.ID)
            .filter(
                extract('month', XUAT_CHIEU.Ngay_Chieu) == Thang,
                extract('year', XUAT_CHIEU.Ngay_Chieu) == Nam
            )
            .group_by(
                CA.ID,
                CA.Bat_Dau,
                CA.Ket_Thuc,
                CA.Ten,
            )
            .all()
        )
        
        Phan_Hoi = {
            "Thang" : Thang,
            "Nam" : Nam,
            "Tong_So_Ve": None,
            "Danh_Sach_Tong_Ve_Theo_Ca": None
        }
        if Danh_Sach_Tong_Ve_Theo_Ca:
            Phan_Hoi["Tong_So_Ve"] = Nghiep_Vu_Thong_Ke_Ve.Tong_So_Ve(Danh_Sach_Tong_Ve_Theo_Ca)
            Phan_Hoi["Danh_Sach_Tong_Ve_Theo_Ca"] = Giao_Tiep_Ve_Theo_Ca.Danh_Sach(Danh_Sach_Tong_Ve_Theo_Ca)
            
        return jsonify(Phan_Hoi)
        