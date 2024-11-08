
from datetime import datetime
class Giao_Tiep_Xuat_Chieu:
    @staticmethod
    def Doi_Tuong(xuat_chieu):
        if not xuat_chieu:
            return None
        
        Ket_Qua = {
            "ID" : xuat_chieu.ID,
            "Ngay_Chieu": datetime.strftime(xuat_chieu.Ngay_Chieu, '%d-%m-%Y'),
            "Don_Gia": xuat_chieu.Don_Gia,
            "Trang_Thai": xuat_chieu.Trang_Thai
        }
        if xuat_chieu.Phim:
            from XL_Giao_Tiep.Giao_Tiep_Phim import Giao_Tiep_Phim
            Ket_Qua["Phim"] = Giao_Tiep_Phim.Doi_Tuong(xuat_chieu.Phim)
        if xuat_chieu.Ca:
            from XL_Giao_Tiep.Giao_Tiep_Ca import Giao_Tiep_Ca
            Ket_Qua["Ca"] = Giao_Tiep_Ca.Doi_Tuong(xuat_chieu.Ca)
        if xuat_chieu.Phong:
            from XL_Giao_Tiep.Giao_Tiep_Phong import Giao_Tiep_Phong
            Ket_Qua["Phong"] = Giao_Tiep_Phong.Doi_Tuong(xuat_chieu.Phong)
        if xuat_chieu.Ves:
            from XL_Giao_Tiep.Giao_Tiep_Ve import Giao_Tiep_Ve
            Ket_Qua["Ves"] = Giao_Tiep_Ve.Danh_Sach(xuat_chieu.Ves)
            
        return Ket_Qua
    
    @staticmethod
    def Danh_Sach(xuat_chieus):
        return [Giao_Tiep_Xuat_Chieu.Doi_Tuong(xuat_chieu) for xuat_chieu in xuat_chieus]
    
    