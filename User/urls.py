from django.urls import path, include
from .views import *

# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register('admin', Admin_Update, basename='admin')


urlpatterns = [
    path('view/', User_View.as_view(), name='user-view'),
    path('register/', User_Register.as_view(), name='user-register'),
    path('login/', User_Login.as_view(), name='user-login'),
    path('home/', User_Home.as_view(), name='user-home'),
    path('send-email/<int:id>/', Send_Mail.as_view()),

    path('user-logout/', logout_view)
]
