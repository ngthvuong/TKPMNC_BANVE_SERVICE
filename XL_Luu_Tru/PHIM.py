from . import db

class PHIM(db.Model):
    
    __tablename__ = "PHIM"
    
    ID = db.Column(db.Integer, primary_key=True)
    Ten = db.Column(db.String(255), nullable=False)
    
    Xuat_Chieus = db.relationship("XUAT_CHIEU", back_populates="Phim", cascade="all, delete-orphan", lazy="noload")
    
    def __repr__(self):
        return f'<PHIM {self.Ten}>'
    