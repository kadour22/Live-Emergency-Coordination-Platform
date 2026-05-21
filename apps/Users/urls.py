from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
 
urlpatterns= [

    path("token/", TokenObtainPairView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),

    path("user-service/", views.UserServiceView.as_view())
]