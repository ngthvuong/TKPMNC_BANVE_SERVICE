
class UserResource:
    @staticmethod
    def resource(user):
        return {
            "id" : user.id,
            "username": user.username
        }
    
    @staticmethod
    def list_resources(users):
        return [UserResource.resource(user) for user in users]
    
    