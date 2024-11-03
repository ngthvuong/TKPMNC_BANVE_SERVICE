from flask import Blueprint
from XL_Bien_Co.user_controller import UserController

user_bp = Blueprint("user", __name__, url_prefix="/users")
user_controller = UserController()

@user_bp.route("/", methods=['POST'])
def create_user():
    return user_controller.create()

@user_bp.route("/", methods=['GET'])
def get_all_users():
    return user_controller.get_all()