
class Giao_Tiep_Nhan_Vien:
    @staticmethod
    def Doi_Tuong(nhan_vien):
        if not nhan_vien:
            return None
        return {
            "id" : nhan_vien.ID,
            "email": nhan_vien.Email,
            "Mat_Khau": nhan_vien.Mat_Khau,
            "Ho_Ten": nhan_vien.Ho_Ten
        }
    
    @staticmethod
    def Danh_Sach(nhan_viens):
        return [Giao_Tiep_Nhan_Vien.resource(nhan_vien) for nhan_vien in nhan_viens]
    
    