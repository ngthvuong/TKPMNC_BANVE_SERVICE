
class Nhan_Vien_Resource:
    @staticmethod
    def resource(nhan_vien):
        if not nhan_vien:
            return None
        return {
            "id" : nhan_vien.ID,
            "email": nhan_vien.Email,
            "Mat_Khau": nhan_vien.Mat_Khau,
            "Ho_Ten": nhan_vien.Ho_Ten
        }
    
    @staticmethod
    def list_resources(nhan_viens):
        return [Nhan_Vien_Resource.resource(nhan_vien) for nhan_vien in nhan_viens]
    
    