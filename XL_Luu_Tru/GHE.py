from . import db

class GHE(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Ten = db.Column(db.String(255), nullable=False)
    
    Phong_ID = db.Column(db.Integer, db.ForeignKey("PHONG.ID"), nullable=False)
    
    Phong = db.relationship("PHONG", back_populates="Ghes", cascade="all, delete-orphan")
    
    Ves = db.relationship("VE", back_populates="Ghe")