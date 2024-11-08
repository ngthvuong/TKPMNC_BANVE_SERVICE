
class Giao_Tiep_Rap:
    @staticmethod
    def Doi_Tuong(rap):
        if not rap:
            return None
        return {
            "ID" : rap.ID,
            "Ten" : rap.Ten,
            "Dia_Chi": rap.Dia_Chi,
        }
    
    @staticmethod
    def Danh_Sach(raps):
        return [Giao_Tiep_Rap.Doi_Tuong(rap) for rap in raps]
    
    