from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import test_serializer

class test_view(APIView) :

    def get(self, request) :
        return Response({"message":"API working.."})

    def post(self, request) :
        serializer = test_serializer(data = request.data)
        if serializer.is_valid() :
            return Response("data added")
        return Response(serializer.errors)