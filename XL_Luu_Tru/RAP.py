from . import db

class RAP(db.Model):
    
    __tablename__="RAP"
    
    ID = db.Column(db.Integer, primary_key=True)
    Ten = db.Column(db.String(255), nullable=False)
    Dia_Chi = db.Column(db.Text, nullable=False)
    
    Quan_Ly_ID = db.Column(db.Integer, db.ForeignKey("NHAN_VIEN.ID"), nullable=True)
    CONG_TY_ID = db.Column(db.Integer, db.ForeignKey("CONG_TY.ID"), nullable=False)
    
    Quan_Ly = db.relationship("NHAN_VIEN", back_populates="Raps")
    Cong_Ty = db.relationship("CONG_TY", back_populates="Raps")
    
    Phongs = db.relationship("PHONG", back_populates="Rap", cascade="all, delete-orphan")