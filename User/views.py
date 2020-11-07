from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import User
from .serializations import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from django.contrib import auth

from .user_decorator import user_login
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from Service.models import Service
import smtplib

# Create your views here.


class User_View(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'user_list.html'
    @user_login
    def get(self, request):
        uname = request.session.get('user')
        users = User.objects.all()
        return Response({'users': users, 'user': uname})


class User_Register(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'user_register.html'

    def get(self, request):
        serializer = UserSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('/user/login/')


class User_Login(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'user_login.html'

    def get(self, request):
        serializer = LoginSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            try:
                user = User.objects.get(
                    user_username__exact=username, user_password__exact=password)
                if user is not None:

                    request.session['user'] = user.user_username
                    request.session['userid'] = user.user_id
                    request.session['useremail'] = user.user_email
                    return redirect('/user/home/')
            except AttributeError:
                return Response('User Not Present')
        return redirect('/user/login/')


# User Logout
def logout_view(request):
    auth.logout(request)
    return redirect('/')


class User_Guest(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'userguest.html'
    objservice = Service.objects.all()

    def get(self, request):
        return Response({'objservice': self.objservice})


class User_Home(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'user_home.html'

    objservice = Service.objects.all()

    def get(self, request):
        userid = request.session.get('userid')
        user = request.session.get('user')
        return Response({'objservice': self.objservice, 'user': user})


# Plese flow this link : https://www.google.com/settings/security/lesssecureapps


class Send_Mail(APIView):
    def post(self, request, id):
        # user_email = request.session.get('useremail')

        userid = request.session.get('userid')
        username = request.session.get('user')
        sender_email = 'crfansclub7@gmail.com'
        service = Service.objects.get(service_id=id)
        rec_email = service.service_email
        password = 'password@7'
        message = f'Hello Sir, I am {username}. Please provide service to me!!!'
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, rec_email, message)
        return HttpResponse(f'Email has been sent to  {rec_email}  ')
