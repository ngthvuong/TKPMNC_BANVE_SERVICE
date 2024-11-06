from flask import Blueprint

Xac_Thuc_BP = Blueprint("xacthuc", __name__, url_prefix="/xacthuc")

@Xac_Thuc_BP.route("/", methods=['GET'])
def get():
    return "hihi"