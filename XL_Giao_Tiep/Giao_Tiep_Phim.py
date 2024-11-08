

class Giao_Tiep_Phim:
    @staticmethod
    def Doi_Tuong(phim):
        if not phim:
            return None
        Ket_Qua = {
            "ID" : phim.ID,
            "Ten": phim.Ten
        }
        if phim.Xuat_Chieus:
            from .Giao_Tiep_Xuat_Chieu import Giao_Tiep_Xuat_Chieu
            Ket_Qua["Xuat_Chieus"] = Giao_Tiep_Xuat_Chieu.Danh_Sach(phim.Xuat_Chieus)
        
        return Ket_Qua
    
    @staticmethod
    def Danh_Sach(phims):
        return [Giao_Tiep_Phim.Doi_Tuong(phim) for phim in phims]
    
    