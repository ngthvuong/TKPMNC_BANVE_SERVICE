import os
from flask import Flask
from XL_Luu_Tru import db
from Du_Lieu.Tao_Du_Lieu import Tao_Du_Lieu
from Dinh_Tuyen import init_routes

from flask_jwt_extended import create_access_token, JWTManager, jwt_required, get_jwt_identity


app = Flask(__name__)

base_dir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(base_dir, "Du_Lieu", "Ban_Ve_Xem_Phim.db")

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


app.config['JWT_SECRET_KEY'] = 'A0F%tX59Q1'
jwt = JWTManager(app)

@app.route("/")
def home():
    return "hello, Flask"

init_routes(app)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        Tao_Du_Lieu()
        access_token = create_access_token(identity="123456789")
        print(access_token)
    app.run(debug=True, port=6102)
    