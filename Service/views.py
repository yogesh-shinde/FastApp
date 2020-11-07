from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Service
from .serializations import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from django.contrib import auth

from User.user_decorator import user_login


class MyService(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'myservice.html'

    @user_login
    def get(self, request):
        userid = request.session.get('userid')
        user = request.session.get('user')
        services = Service.objects.filter(user__user_id=userid)
        return Response({'services': services, 'user': user})


class AddService(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'add_service.html'
    @user_login
    def get(self, request):
        userid = request.session.get('userid')
        serializers = ServiceSerializer()
        user = request.session.get('user')
        return Response({'serializers': serializers, 'user': user})

    @user_login
    def post(self, request):
        serializers = ServiceSerializer(data=request.data)

        if serializers.is_valid():
            serializers.save()
        return redirect('/service/display-service/')


# Display the service and send to the admin
class DisplayService(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'display_service.html'

    @user_login
    def get(self, request):
        userid = request.session.get('userid')
        user = request.session.get('user')
        services = Service.objects.filter(user__user_id=userid)
        return Response({'services': services, 'user': user})
