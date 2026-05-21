from rest_framework.views import APIView
from rest_framework.response import Response
from .services.user_services import UserService

class CreateUserServiceView(APIView) :
    def __init__(*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_service = UserService()
    
    def post(self,request):
        create_user = self.user_service.create_new_user(data=request.data)
        return Response(create_user)
    
    def patch(self, request):
        result = self.user_service.change_user_password(
            data=request.data,
            user=request.user
        )
        return Response(result)