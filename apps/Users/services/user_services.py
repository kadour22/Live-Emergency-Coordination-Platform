from django.contrib.auth.models import User
from apps.Users.serializers import user_serializer, ChangePasswordSerializer
class UserService :

    def create_new_user(self, data) :

        serializer = user_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.save()
        return {
            "new_user_data": user_serializer(user_data).data
        }
    
    def change_user_password(self, data, user):
        serializer = ChangePasswordSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        user.set_password(serializer.validated_data["new_password"])
        user.save()

        return {
            "message": "Password updated successfully"
        }