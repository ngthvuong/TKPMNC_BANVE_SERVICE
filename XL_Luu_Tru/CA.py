from . import db

class CA(db.Model):
    
    __tablename__ = "CA"
    
    ID = db.Column(db.Integer, primary_key=True)
    Ten = db.Column(db.String(255), nullable=False)
    Bat_Dau = db.Column(db.String(5), nullable=False)
    Ket_Thuc = db.Column(db.String(5), nullable=False)
    
    Xuat_Chieus = db.relationship("XUAT_CHIEU", back_populates="Ca")
    
    def __repr__(self):
        return f'<CA {self.Ten}>'