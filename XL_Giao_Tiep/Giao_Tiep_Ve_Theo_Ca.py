
class Giao_Tiep_Ve_Theo_Ca:
    @staticmethod
    def Doi_Tuong(Ve_Theo_Ca):
        if not Ve_Theo_Ca:
            return None
        
        Ket_Qua = {
            "ID" : Ve_Theo_Ca.ID,
            "Ten": Ve_Theo_Ca.Ten,
            "Bat_Dau": Ve_Theo_Ca.Bat_Dau,
            "Ket_Thuc": Ve_Theo_Ca.Ket_Thuc,
            "So_Luong_Ve": Ve_Theo_Ca.So_Luong_Ve,
        }          
        
        return Ket_Qua
    
    @staticmethod
    def Danh_Sach(Ve_Theo_Cas):
        return [Giao_Tiep_Ve_Theo_Ca.Doi_Tuong(Ve_Theo_Ca) for Ve_Theo_Ca in Ve_Theo_Cas]
    
    