from . import db

class PHIM(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Ten = db.Column(db.String(255), nullable=False)
    
    Xuat_Chieus = db.relationship("XUAT_CHIEU", back_populates="Phim")
    