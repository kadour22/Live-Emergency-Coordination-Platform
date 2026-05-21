from django.contrib.auth.models import User
from ..serializers import user_serialier, ChangePasswordSerializer

class UserService :

    def create_new_user(self, data) :

        serializer = user_serialier(data=data)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.save()
        return {
            "new_user_data": user_serialier(user_data).data
        }
    
    def change_user_password(self,data,user) :

        serializer = ChangePasswordSerializer(data=data)
        if serializer.is_valid() :
            user.set_password(serializer.validatd_data["new_password"])
            user.save()
            return {
                "message": "Password updated successfully"
            }
        return {
            "error":"error"
        }