
class Giao_Tiep_Ghe:
    @staticmethod
    def Doi_Tuong(ghe):
        if not ghe:
            return None
        return {
            "ID" : ghe.ID,
            "Ten": ghe.Ten,
        }
    
    @staticmethod
    def Danh_Sach(ghes):
        return [Giao_Tiep_Ghe.Doi_Tuong(ghe) for ghe in ghes]
    
    