from XL_Luu_Tru import db
from XL_Luu_Tru.CONG_TY import CONG_TY
from XL_Luu_Tru.LOAI_PHONG import LOAI_PHONG
from XL_Luu_Tru.CA import CA
from XL_Luu_Tru.PHIM import PHIM
from XL_Luu_Tru.NHAN_VIEN import NHAN_VIEN
from XL_Luu_Tru.RAP import RAP
from XL_Luu_Tru.PHONG import PHONG
from XL_Luu_Tru.GHE import GHE
from XL_Luu_Tru.XUAT_CHIEU import XUAT_CHIEU
from XL_Luu_Tru.VE import VE

import random
from datetime import datetime, timedelta
from sqlalchemy.orm import joinedload

def Tao_Du_Lieu():
    if db.session.query(NHAN_VIEN).first():
        return
    # Thêm công ty
    print("Dang them CONG_TY")
    congty = CONG_TY(
        Ten = "FunCipher Cinema",
        Dia_Chi = "148 Huỳnh Thị Na, Đông Thạnh, Hóc Môn, TP.HCM",
        Dien_Thoai="0909976102"
    )
    db.session.add(congty)
    
    # Thêm loại phòng
    print("Dang them LOAI_PHONG")
    phong_loai_1 = LOAI_PHONG(Ten="Loại 1", So_Ghe=100, So_Day=10)
    phong_loai_2 = LOAI_PHONG(Ten="Loại 2", So_Ghe=60, So_Day=6)
    db.session.add(phong_loai_1)
    db.session.add(phong_loai_2)
    
    # Thêm ca chiếu
    print("Dang them CA")
    ca_1 = CA(Ten="Sáng", Bat_Dau="09h00", Ket_Thuc="11h00")
    ca_2 = CA(Ten="Chiều", Bat_Dau="14h00", Ket_Thuc="16h00")
    ca_3 = CA(Ten="Tối", Bat_Dau="18h00", Ket_Thuc="20h00")
    ca_4 = CA(Ten="Tối", Bat_Dau="20h30", Ket_Thuc="22h30")
    db.session.add(ca_1)
    db.session.add(ca_2)
    db.session.add(ca_3)
    db.session.add(ca_4)
    
    # Thêm phim
    print("Dang them PHIM")
    phims = [
        PHIM(Ten="Mùa hè lạnh"),
        PHIM(Ten="Cô gái đến từ hôm qua"),
        PHIM(Ten="Em chưa 18"),
        PHIM(Ten="Tiệc trăng máu"),
        PHIM(Ten="Chị chị em em"),
        PHIM(Ten="Nhà Bà Nữ"),
        PHIM(Ten="Tôi thấy hoa vàng trên cỏ xanh"),
        PHIM(Ten="Dòng máu anh hùng"),
        PHIM(Ten="Bình minh trắng"),
        PHIM(Ten="Bẫy ngọt ngào"),
        PHIM(Ten="Ròm"),
        PHIM(Ten="Thưa mẹ con đi"),
        PHIM(Ten="Trạng Tí"),
        PHIM(Ten="Gái Già Lắm Chiêu"),
        PHIM(Ten="Sống chung với mẹ chồng"),
        PHIM(Ten="Chạy đi rồi tính"),
        PHIM(Ten="Người bất tử"),
        PHIM(Ten="Dân gian"),
        PHIM(Ten="Cua lại vợ bầu"),
        PHIM(Ten="Ngày mai mai cưới"),
        PHIM(Ten="Yêu đi, đừng sợ"),
        PHIM(Ten="Lật mặt: Nhà có khách"),
        PHIM(Ten="Quả tim máu"),
        PHIM(Ten="Kẻ cắp gặp bà già"),
        PHIM(Ten="Người thứ 3"),
        PHIM(Ten="Tháng năm rực rỡ"),
        PHIM(Ten="Khi con là nhà"),
        PHIM(Ten="Làm dâu thời đại"),
        PHIM(Ten="Mong manh giấc mơ"),
        PHIM(Ten="Cơn mưa của bầu trời"),
        PHIM(Ten="Harry Potter và Hòn đá phù thủy"),
        PHIM(Ten="Inception"),
        PHIM(Ten="Bố già"),
        PHIM(Ten="Titanic"),
        PHIM(Ten="Kẻ đào tẩu"),
        PHIM(Ten="Chạy đi, đừng dừng lại"),
        PHIM(Ten="Công viên kỷ Jura"),
        PHIM(Ten="Kỵ sĩ bóng đêm"),
        PHIM(Ten="Chuyện kinh dị Pulp"),
        PHIM(Ten="Cuộc chiến sinh tử"),
        PHIM(Ten="Ma trận"),
        PHIM(Ten="Đấu trường sinh tử"),
        PHIM(Ten="Giữa các vì sao"),
        PHIM(Ten="Vua sư tử"),
        PHIM(Ten="Danh sách của Schindler"),
        PHIM(Ten="Avatar"),
        PHIM(Ten="Nữ hoàng băng giá"),
        PHIM(Ten="Người nhện: Vũ trụ mới"),
        PHIM(Ten="Biệt đội siêu anh hùng"),
        PHIM(Ten="Star Wars: Hi vọng mới"),
        PHIM(Ten="La La Land"),
        PHIM(Ten="Ký sinh trùng"),
        PHIM(Ten="Tên của bạn"),
        PHIM(Ten="Chúa tể của những chiếc nhẫn: Hiệp hội chiếc nhẫn"),
        PHIM(Ten="Coco"),
        PHIM(Ten="Người hùng của vương quốc"),
        PHIM(Ten="Mad Max: Con đường điên cuồng"),
        PHIM(Ten="Joker"),
        PHIM(Ten="Im lặng của bầy cừu"),
        PHIM(Ten="Giải cứu binh nhì Ryan"),
        PHIM(Ten="Mạng xã hội"),
        PHIM(Ten="Làm trái tim nhút nhát"),
        PHIM(Ten="Nổi tiếng trên mạng"),
        PHIM(Ten="Khi em ở nhà"),
        PHIM(Ten="Điều ước của tôi"),
        PHIM(Ten="Hành trình tuyệt vời"),
        PHIM(Ten="Một thế giới hoàn hảo"),
        PHIM(Ten="Chuyến tàu kỳ diệu"),
        PHIM(Ten="Giấc mơ trở thành hiện thực"),
        PHIM(Ten="Cuộc sống của bạn"),
        PHIM(Ten="Cuộc phiêu lưu của bạn"),
        PHIM(Ten="Cuộc sống thần kỳ"),
        PHIM(Ten="Cuộc sống tươi đẹp"),
        PHIM(Ten="Hành trình về nhà"),
        PHIM(Ten="Thế giới của chúng ta"),
        PHIM(Ten="Điều kỳ diệu của cuộc sống"),
    ]
    for phim in phims:
        db.session.add(phim)
    
    # Thêm nhân viên
    print("Dang them NHAN_VIEN")
    nhan_viens = [
        NHAN_VIEN(Ho_Ten = "Nguyễn Văn Tí Ròm", Email="ti_rom@gmail.com", Mat_Khau="!234qweR", Vai_Tro= "Quan_Ly_Rap"),
        NHAN_VIEN(Ho_Ten = "Lê Văn Tí Cao", Email="ti_cao@gmail.com", Mat_Khau="!234qweR", Vai_Tro= "Nhan_Vien_Ban_Ve"),
        NHAN_VIEN(Ho_Ten = "Lý Thị Tí Tẹo", Email="ti_teo@gmail.com", Mat_Khau="!234qweR", Vai_Tro= "Nhan_Vien_Ban_Ve"),
        NHAN_VIEN(Ho_Ten = "Trần Thị Tí Nị", Email="ti_ni@gmail.com", Mat_Khau="!234qweR", Vai_Tro= "Quan_Ly_Rap"),
        NHAN_VIEN(Ho_Ten = "Dương Văn Tí Mập", Email="ti_map@gmail.com", Mat_Khau="!234qweR", Vai_Tro= "Nhan_Vien_Ban_Ve"),
        NHAN_VIEN(Ho_Ten = "Ngô Thị Tí Mèo", Email="ti_meo@gmail.com", Mat_Khau="!234qweR", Vai_Tro= "Nhan_Vien_Ban_Ve"),
    ]
    congty.Nhan_Viens.extend(nhan_viens)
    db.session.commit()
    
    nhan_vien_quan_ly = db.session.query(NHAN_VIEN).filter(NHAN_VIEN.Vai_Tro == "Quan_Ly_Rap").all()
    

    # Thêm rạp
    print("Dang them RAP")
    raps = [
        RAP(Ten = "PHP Cinema", Dia_Chi = "101 Le Lai, Ben Thanh, Q1, TP.HCM", Quan_Ly_ID = nhan_vien_quan_ly[0].ID),
        RAP(Ten = "Javascript Cinema", Dia_Chi = "202 Nguyen Thi Minh Khai, Q3, TP.HCM", Quan_Ly_ID = nhan_vien_quan_ly[0].ID),
        RAP(Ten = "Python Cinema", Dia_Chi = "123 Nguyen Trai, Q1, TP.HCM", Quan_Ly_ID = nhan_vien_quan_ly[1].ID),
        RAP(Ten = "C# Cinema", Dia_Chi = "303 Vo Van Tan, Q3, TP.HCM", Quan_Ly_ID = nhan_vien_quan_ly[0].ID),
        RAP(Ten = "C++ Cinema", Dia_Chi = "505 Nguyen Hue, Ben Nghe, Q1, TP.HCM", Quan_Ly_ID = nhan_vien_quan_ly[1].ID),
    ]
    
    # Thêm phòng
    print("Dang them PHONG va GHE")
    loai_phong = db.session.query(LOAI_PHONG).all()
    for rap in raps:
        prefix = rap.Ten.split(" ")[0]
        random_number = random.randint(5,7)
        rap.Phongs = [
            PHONG(Ten = f"Roon {prefix} {i + 1}", Loai_Phong_ID = random.choice(loai_phong).ID) for i in range(random_number)
        ]
    
        # Thêm ghế
        for phong in rap.Phongs:
            so_ghe = next((lp.So_Ghe for lp in loai_phong if lp.ID == phong.Loai_Phong_ID), None)
            phong.Ghes = [
                GHE(Ten = f"Ghế Số {i+1}") for i in range(so_ghe)
            ]
    congty.Raps.extend(raps)
    db.session.commit()
    
    #Thêm xuất chiếu
    print("Dang them XUAT_CHIEU")
    ngay_bat_dau = datetime.strptime("2023-11-01", "%Y-%m-%d")
    cas = db.session.query(CA).all()
    phongs = db.session.query(PHONG).all()
    phims = db.session.query(PHIM).all()
    for i in range(400):
        ngay_muc_tieu = ngay_bat_dau + timedelta(days = i)
        cac_phim_theo_giai_doan = phims[0:10]
        for ca in cas:
            for phong in phongs:
                if(random.randint(0,2)):
                    phim = random.choice(cac_phim_theo_giai_doan)
                    xuat_chieu = XUAT_CHIEU(
                        Ngay_Chieu=ngay_muc_tieu.date(),
                        Don_Gia=80000,
                        Phong_ID=phong.ID,
                        Phim_ID=phim.ID,
                        Ca_ID=ca.ID
                    )
                    db.session.add(xuat_chieu)
    db.session.commit()
    
    #Thêm vé
    print("Dang them VE")
    limit_date = datetime.strptime("2024-12-10", "%Y-%m-%d").date()
    xuat_chieus = (
        db.session
        .query(XUAT_CHIEU)
        .filter(XUAT_CHIEU.Ngay_Chieu <= limit_date)
        .options(
            joinedload(XUAT_CHIEU.Phong).joinedload(PHONG.Ghes),
            joinedload(XUAT_CHIEU.Phong).joinedload(PHONG.Loai_Phong)
        )
        .all()
    )
    for xuat_chieu in xuat_chieus:
        range_random = 100 if xuat_chieu.Phong.Loai_Phong.Ten == "Loại 1" else 60
        random_number = random.randint(10, range_random - 20)
        for i in range(random_number):
            ve = VE(
                Gia = xuat_chieu.Don_Gia,
                Xuat_Chieu_ID = xuat_chieu.ID,
                Ghe_ID = xuat_chieu.Phong.Ghes[i].ID
            )
            db.session.add(ve)
            
    db.session.commit()