
class Giao_Tiep_Ca:
    @staticmethod
    def Doi_Tuong(ca):
        if not ca:
            return None
        return {
            "ID" : ca.ID,
            "Ten": ca.Ten,
            "Bat_Dau": ca.Bat_Dau,
            "Ket_Thuc": ca.Ket_Thuc,
        }
    
    @staticmethod
    def Danh_Sach(cas):
        return [Giao_Tiep_Ca.Doi_Tuong(ca) for ca in cas]
    
    