from . import db
class PHONG(db.Model):
    
    __tablename__="PHONG"
    
    ID = db.Column(db.Integer, primary_key=True)
    Ten = db.Column(db.String(255), nullable=False)
    
    Rap_ID = db.Column(db.Integer, db.ForeignKey("RAP.ID"), nullable=False)
    Loai_Phong_ID = db.Column(db.Integer, db.ForeignKey("LOAI_PHONG.ID"), nullable=False)
    
    Rap = db.relationship("RAP", back_populates="Phongs")
    Loai_Phong = db.relationship("LOAI_PHONG", back_populates="Phongs")
    
    Ghes = db.relationship("GHE", back_populates="Phong", cascade="all, delete-orphan")
    Xuat_Chieus = db.relationship("XUAT_CHIEU", back_populates="Phong", cascade="all, delete-orphan")
    