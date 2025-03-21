from . import db

class VE(db.Model):
    
    __tablename__ = "VE"
    
    ID = db.Column(db.Integer, primary_key=True)
    Gia = db.Column(db.Integer, nullable=False)
    
    Ghe_ID = db.Column(db.Integer, db.ForeignKey("GHE.ID"), nullable=True)
    Xuat_Chieu_ID = db.Column(db.Integer, db.ForeignKey("XUAT_CHIEU.ID"), nullable=True)
    
    Ghe = db.relationship("GHE", back_populates="Ves", lazy="noload")
    Xuat_Chieu = db.relationship("XUAT_CHIEU", back_populates="Ves", lazy="noload")
    
    def __repr__(self):
        return f'<VE {self.ID} {self.Gia}>'
    