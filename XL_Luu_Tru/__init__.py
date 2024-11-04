from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .CONG_TY import CONG_TY
from .NHAN_VIEN import NHAN_VIEN
from .RAP import RAP
from .LOAI_PHONG import LOAI_PHONG
from .PHONG import PHONG
from .GHE import GHE
from .CA import CA
from .PHIM import PHIM
from .XUAT_CHIEU import XUAT_CHIEU
from .VE import VE

