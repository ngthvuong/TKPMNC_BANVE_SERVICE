
class Giao_Tiep_Loai_Phong:
    @staticmethod
    def Doi_Tuong(loai_phong):
        if not loai_phong:
            return None
        return {
            "ID" : loai_phong.ID,
            "Ten" : loai_phong.Ten,
            "So_Ghe": loai_phong.So_Ghe,
            "So_Day": loai_phong.So_Day,
            
        }
    
    @staticmethod
    def Danh_Sach(loai_phongs):
        return [Giao_Tiep_Loai_Phong.Doi_Tuong(loai_phong) for loai_phong in loai_phongs]
    
    