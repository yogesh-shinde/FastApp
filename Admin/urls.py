from django.urls import path, include
from .views import *

# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register('admin', Admin_Update, basename='admin')


urlpatterns = [
    path('view/', Admin_View.as_view(), name='admin-view'),
    path('register/', Admin_Register.as_view(), name='admin-register'),
    path('login/', Admin_Login.as_view(), name='admin-login'),

    path('pending-verification/', PendingVerification.as_view()),
    path('service-verified/', ServiceVerified.as_view()),

    path('admin-verifyproduct/<int:id>/', VerifyProduct.as_view()),
    path('admin-cancelproduct/<int:id>/', CancelService.as_view()),



    # # View set
    # path('viewset/', include(router.urls)),
    # path('viewset/<int:pk>/', include(router.urls)),


]
