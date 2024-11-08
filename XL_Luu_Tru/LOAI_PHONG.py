from . import db

class LOAI_PHONG(db.Model):
    
    __tablename__ = "LOAI_PHONG"
    
    ID = db.Column(db.Integer, primary_key=True)
    Ten = db.Column(db.String(50), nullable=False)
    So_Ghe = db.Column(db.Integer, nullable=False)
    So_Day = db.Column(db.Integer, nullable=False)
    
    Phongs = db.relationship("PHONG", back_populates="Loai_Phong", lazy="noload")
    
    def __repr__(self):
        return f'<LOAI_PHONG {self.Ten}>'