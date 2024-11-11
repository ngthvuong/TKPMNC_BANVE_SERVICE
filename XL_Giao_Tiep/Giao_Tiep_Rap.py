
class Giao_Tiep_Rap:
    @staticmethod
    def Doi_Tuong(rap):
        if not rap:
            return None
        Ket_Qua = {
            "ID" : rap.ID,
            "Ten" : rap.Ten,
            "Dia_Chi": rap.Dia_Chi,
        }
        if rap.Phongs:
            from XL_Giao_Tiep.Giao_Tiep_Phong import Giao_Tiep_Phong
            Ket_Qua["Phongs"] = Giao_Tiep_Phong.Danh_Sach(rap.Phongs)
        
        return Ket_Qua
    
    @staticmethod
    def Danh_Sach(raps):
        return [Giao_Tiep_Rap.Doi_Tuong(rap) for rap in raps]
    
    