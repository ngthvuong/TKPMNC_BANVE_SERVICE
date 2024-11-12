import os
from flask import Flask
from XL_Luu_Tru import db
from Du_Lieu.Tao_Du_Lieu import Tao_Du_Lieu
from Dinh_Tuyen import init_routes

app = Flask(__name__)

base_dir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(base_dir, "Du_Lieu", "Ban_Ve_Xem_Phim.db")

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

init_routes(app)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        Tao_Du_Lieu()
    app.run(debug=True, port=6102)
    