from flask import request, jsonify
from XL_Luu_Tru.user import User
from XL_Luu_Tru import db

from XL_Giao_Tiep.user_resource import UserResource

class UserController:
    def create(self):
        data = request.get_json()
        username = data.get('username')
        
        new_user = User(username=username)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully!"})
    
    def get_all(self):
        users = User.query.all()
        return jsonify({"data": UserResource.list_resources(users)})