from XL_Luu_Tru import db
from XL_Luu_Tru.CONG_TY import CONG_TY
from XL_Luu_Tru.RAP import RAP

def Tao_Du_Lieu():
    # them cong ty
    congty = CONG_TY(
        Ten = "Fun Cipher Cinema",
        Dia_Chi = "148 Huỳnh Thị Na, Đông Thạnh, Hóc Môn, TP.HCM",
        Dien_Thoai="0909976102"
    )
    db.session.add(congty)
    
    raps = [
        RAP(Ten = "Rạp 1", Dia_Chi = "123 Nguyen Trai, Q1, TP.HCM"),
        RAP(Ten = "RAP 2", Dia_Chi = "456 Tran Hung Dao, Q5, TP.HCM")
    ]
    
    congty.Raps.extend(raps)
    
    db.session.commit()