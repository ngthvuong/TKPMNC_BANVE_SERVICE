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
            )
            .filter(
                XUAT_CHIEU.Ngay_Chieu >= datetime.today()
            )
            .all()
        )
        return jsonify(Giao_Tiep_Xuat_Chieu.Danh_Sach(Xuat_Chieus))

    def Lay_Danh_Sach_Chua_Chieu_Theo_Quan_Ly(self, Quan_Ly_ID):
        Xuat_Chieus = (
            db.session.query(XUAT_CHIEU)
            .options(
                joinedload(XUAT_CHIEU.Phim),
                joinedload(XUAT_CHIEU.Ca),
                joinedload(XUAT_CHIEU.Phong).joinedload(PHONG.Loai_Phong),
                joinedload(XUAT_CHIEU.Phong).joinedload(PHONG.Rap),
            )
            .filter(
                XUAT_CHIEU.Phong.has(PHONG.Rap.has(RAP.Quan_Ly_ID == Quan_Ly_ID)),
                XUAT_CHIEU.Ngay_Chieu >= date.today()
            )
            .order_by(XUAT_CHIEU.Ngay_Chieu.desc())
            .all()
        )
        return jsonify(Giao_Tiep_Xuat_Chieu.Danh_Sach(Xuat_Chieus))    

    def Lay_Xuat_Chieu(self):
        ID = request.args.get('ID')
        Xuat_Chieu = (
            db.session.query(XUAT_CHIEU)
            .options(
                joinedload(XUAT_CHIEU.Phim),
                joinedload(XUAT_CHIEU.Ca),
                joinedload(XUAT_CHIEU.Phong).joinedload(PHONG.Loai_Phong),
                joinedload(XUAT_CHIEU.Phong).joinedload(PHONG.Rap),
                joinedload(XUAT_CHIEU.Phong).joinedload(PHONG.Ghes),
                joinedload(XUAT_CHIEU.Ves).joinedload(VE.Ghe),
            )
            .filter(
                XUAT_CHIEU.ID == ID
            )
            .first()
        )
        return jsonify(Giao_Tiep_Xuat_Chieu.Doi_Tuong(Xuat_Chieu))
    
    def Them_Xuat_Chieu(self):
        Yeu_Cau = request.get_json()
        
        try:
            Ngay_Chieu = datetime.strptime(Yeu_Cau.get('Ngay_Chieu'), "%Y-%m-%d").date()
        except ValueError:
            return jsonify({"error": "Định dạng ngày chiếu không đúng" })
        
        Don_Gia = Yeu_Cau.get('Don_Gia')
        Phim_ID = Yeu_Cau.get('Phim_ID')
        Ca_ID = Yeu_Cau.get('Ca_ID')
        Phong_ID = Yeu_Cau.get('Phong_ID')
        
        Xuat_Chieu = (
            db.session.query(XUAT_CHIEU)
            .filter(
                XUAT_CHIEU.Phong_ID == Phong_ID,
                XUAT_CHIEU.Ca_ID == Ca_ID,
                XUAT_CHIEU.Ngay_Chieu == Ngay_Chieu,
            )
            .first()
        )
        if Xuat_Chieu:
            return jsonify({"error": "Phòng này đã có xuất chiếu cùng thời điểm được tạo!" })
        
        Xuat_Chieu_Moi = XUAT_CHIEU(
            Ngay_Chieu=Ngay_Chieu,
            Don_Gia=Don_Gia,
            Phim_ID=Phim_ID,
            Ca_ID=Ca_ID,
            Phong_ID=Phong_ID
        )
        db.session.add(Xuat_Chieu_Moi)
        db.session.commit()

        return jsonify(Giao_Tiep_Xuat_Chieu.Doi_Tuong(Xuat_Chieu_Moi))
    
    def Sua_Xuat_Chieu(self, ID):
        Yeu_Cau = request.get_json()
        
        try:
            Ngay_Chieu = datetime.strptime(Yeu_Cau.get('Ngay_Chieu'), "%Y-%m-%d").date()
        except ValueError:
            return jsonify({"error": "Định dạng ngày chiếu không đúng" })
        
        Don_Gia = Yeu_Cau.get('Don_Gia')
        Phim_ID = Yeu_Cau.get('Phim_ID')
        Ca_ID = Yeu_Cau.get('Ca_ID')
        Phong_ID = Yeu_Cau.get('Phong_ID')
        
        Xuat_Chieu_Trung = (
            db.session.query(XUAT_CHIEU)
            .filter(
                XUAT_CHIEU.Phong_ID == Phong_ID,
                XUAT_CHIEU.Ca_ID == Ca_ID,
                XUAT_CHIEU.Ngay_Chieu == Ngay_Chieu,
                XUAT_CHIEU.ID != ID
            )
            .first()
        )
        if Xuat_Chieu_Trung:
            return jsonify({"error": "Phòng này đã có xuất chiếu cùng thời điểm được tạo!" })
        
        Kiem_Tra_Ve = db.session.query(VE).filter_by(Xuat_Chieu_ID=ID).first()
        if Kiem_Tra_Ve:
            return jsonify({"error": "Không thể sửa xuất chiếu đã bán vé!" })
        
        Xuat_Chieu = db.session.query(XUAT_CHIEU).filter_by(ID=ID).first()
        if not Xuat_Chieu:
            return jsonify({"error": "Xuất chiếu không tồn tại!" })
        
        Xuat_Chieu.Ngay_Chieu = Ngay_Chieu
        Xuat_Chieu.Don_Gia = Don_Gia
        Xuat_Chieu.Phim_ID = Phim_ID
        Xuat_Chieu.Ca_ID = Ca_ID
        Xuat_Chieu.Phong_ID = Phong_ID
        db.session.commit()

        return jsonify(Giao_Tiep_Xuat_Chieu.Doi_Tuong(Xuat_Chieu))
    
    def Xoa_Xuat_Chieu(self, ID):
        Kiem_Tra_Ve = db.session.query(VE).filter_by(Xuat_Chieu_ID=ID).first()
        print(Kiem_Tra_Ve)
        if Kiem_Tra_Ve:
            return jsonify({"error": "Không thể sửa xuất chiếu đã bán vé!"})
        
        Xuat_Chieu = db.session.query(XUAT_CHIEU).filter_by(ID=ID).first()
        if not Xuat_Chieu:
            return jsonify({"error": "Xuất chiếu không tồn tại!"})
        
        db.session.delete(Xuat_Chieu)
        db.session.commit()

        return jsonify({"Message": "Đã xóa xuất chiếu thành công!"})