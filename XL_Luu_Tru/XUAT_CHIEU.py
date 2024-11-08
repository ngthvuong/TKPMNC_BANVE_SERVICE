from . import db

class XUAT_CHIEU(db.Model):
    
    __tablename__ = "XUAT_CHIEU"
    
    ID = db.Column(db.Integer, primary_key=True)
    Ngay_Chieu = db.Column(db.Date, nullable=False, index=True)
    Don_Gia = db.Column(db.Integer, nullable=False)
    Trang_Thai = db.Column(db.Enum("Dang_Mo", "Ket_Thuc"), nullable=False, default="Dang_Mo")
    
    Phong_ID = db.Column(db.Integer, db.ForeignKey("PHONG.ID"), nullable=False)    
    Phim_ID = db.Column(db.Integer, db.ForeignKey("PHIM.ID"), nullable=False)
    Ca_ID = db.Column(db.Integer, db.ForeignKey("CA.ID"), nullable=True)
    
    
    Phong = db.relationship("PHONG", back_populates="Xuat_Chieus", lazy="noload")
    Phim = db.relationship("PHIM", back_populates="Xuat_Chieus", lazy="noload")
    Ca = db.relationship("CA", back_populates="Xuat_Chieus", lazy="noload")
    
    Ves = db.relationship("VE", back_populates="Xuat_Chieu", cascade="all, delete-orphan", lazy="noload")
    
    def __repr__(self):
        return f'<XUAT_CHIEU {self.Ngay_Chieu} {self.Ca_ID}>'
    
    