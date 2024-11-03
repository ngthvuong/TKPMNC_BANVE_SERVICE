from . import db

class LOAI_PHONG(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Ten = db.Column(db.String(50), nullable=False)
    So_Ghe = db.Column(db.Integer, nullable=False)
    So_Day = db.Column(db.Integer, nullable=False)
    
    Phongs = db.relationship("PHONG", back_populates="Loai_Phong")