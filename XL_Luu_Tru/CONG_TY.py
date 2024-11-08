from . import db

class CONG_TY(db.Model):
    
    __tablename__ = "CONG_TY"
    
    ID = db.Column(db.Integer, primary_key=True)
    Ten = db.Column(db.String(50), nullable=False)
    Dia_Chi = db.Column(db.Text, nullable=False)
    Dien_Thoai = db.Column(db.String(15), nullable=False)
    
    Nhan_Viens = db.relationship("NHAN_VIEN", back_populates="Cong_Ty", cascade="all, delete-orphan", lazy="noload")
    Raps = db.relationship("RAP", back_populates="Cong_Ty", cascade="all, delete-orphan", lazy="noload")
    
    def __repr__(self):
        return f'<CONG_TY {self.Ten}>'