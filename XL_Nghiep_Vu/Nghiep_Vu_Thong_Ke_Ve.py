
class Nghiep_Vu_Thong_Ke_Ve:
    @staticmethod
    def Tong_So_Ve(Danh_Sach_Tong_Ve_Theo_Ca):
        Tong_Ve = 0
        if Danh_Sach_Tong_Ve_Theo_Ca:
            Tong_Ve = sum(Thong_Ke.So_Luong_Ve for Thong_Ke in Danh_Sach_Tong_Ve_Theo_Ca)
            
        return Tong_Ve