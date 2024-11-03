from . import db

class VE(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Gia = db.Column(db.Integer, nullable=False)
    Ghe_ID = db.Column(db.Integer, db.ForeignKey("GHE.ID"), nullable=True)
    Xuat_Chieu_ID = db.Column(db.Integer, db.ForeignKey("XUAT_CHIEU.ID"), nullable=True)
    
    Ghe = db.relationship("GHE", back_populates="Ves", cascade="all, delete-orphan")
    Xuat_Chieus = db.relationship("XUAT_CHIEU", back_populates="Ves", cascade="all, delete-orphan")
    