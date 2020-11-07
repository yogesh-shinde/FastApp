from django.urls import path, include
from .views import *


urlpatterns = [
    path('myservice/', MyService.as_view(), name='myservice'),
    path('add-service/', AddService.as_view(), name='add-service'),

    path('display-service/', AddService.as_view(), name='display-service'),

]
