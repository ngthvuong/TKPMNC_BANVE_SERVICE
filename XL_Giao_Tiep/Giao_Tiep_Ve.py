
class Giao_Tiep_Ve:
    @staticmethod
    def Doi_Tuong(ve):
        if not ve:
            return None
        
        Ket_Qua = {
            "ID" : ve.ID,
            "Gia": ve.Gia,
        }
        
        if ve.Ghe:
            from XL_Giao_Tiep.Giao_Tiep_Ghe import Giao_Tiep_Ghe
            Ket_Qua["Ghe"] = Giao_Tiep_Ghe.Doi_Tuong(ve.Ghe)
            
        
        return Ket_Qua
    
    @staticmethod
    def Danh_Sach(ves):
        return [Giao_Tiep_Ve.Doi_Tuong(ve) for ve in ves]
    
    