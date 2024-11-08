
class Giao_Tiep_Phong:
    @staticmethod
    def Doi_Tuong(phong):
        if not phong:
            return None
        Ket_Qua = {
            "ID" : phong.ID,
            "Ten": phong.Ten
        }
        
        if phong.Loai_Phong:
            from XL_Giao_Tiep.Giao_Tiep_Loai_Phong import Giao_Tiep_Loai_Phong
            Ket_Qua["Loai_Phong"] = Giao_Tiep_Loai_Phong.Doi_Tuong(phong.Loai_Phong)
        if phong.Rap:
            from XL_Giao_Tiep.Giao_Tiep_Rap import Giao_Tiep_Rap
            Ket_Qua["Rap"] = Giao_Tiep_Rap.Doi_Tuong(phong.Rap)
        
        return Ket_Qua
    
    @staticmethod
    def Danh_Sach(phongs):
        return [Giao_Tiep_Phong.Doi_Tuong(phong) for phong in phongs]
    
    