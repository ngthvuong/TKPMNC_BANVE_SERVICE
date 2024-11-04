from . import db

class NHAN_VIEN(db.Model):
    
    __tablename__="NHAN_VIEN"
    
    ID = db.Column(db.Integer, primary_key=True)
    Ho_Ten = db.Column(db.String(50), nullable=False)
    Email = db.Column(db.String(255), unique=True, nullable=False)
    Mat_Khau = db.Column(db.String(255), nullable=False)
    Vai_Tro = db.Column(db.Enum("Quan_Ly_Rap", "Nhan_Vien_Ban_Ve"), nullable=False)
    
    Cong_Ty_ID = db.Column(db.Integer, db.ForeignKey("CONG_TY.ID"), nullable=False)
    
    Cong_Ty = db.relationship("CONG_TY", back_populates="Nhan_Viens")

    Raps = db.relationship("RAP", back_populates="Quan_Ly")
    
    def __repr__(self):
        return f'<NHAN_VIEN {self.Email}>'