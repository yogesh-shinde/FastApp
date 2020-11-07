from django.shortcuts import render, redirect, HttpResponse
from .models import Admin
from .serializations import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import get_object_or_404

from .admin_decorator import admin_login
from Service.models import Service
# Create your views here.


class Admin_View(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'admin_list.html'
    @admin_login
    def get(self, request):
        aname = request.session.get('admin')
        admins = Admin.objects.all()
        return Response({'admins': admins, 'admin': aname})


class Admin_Register(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'admin_register.html'

    def get(self, request):
        serializer = AdminSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = AdminSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('/admingui/login/')


class Admin_Login(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'admin_login.html'

    def get(self, request):
        serializer = LoginSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            try:
                admin = Admin.objects.get(
                    admin_username__exact=username, admin_password__exact=password)
                if admin is not None:
                    request.session['admin'] = admin.admin_username
                    request.session['adminid'] = admin.admin_id
                    return redirect('/admingui/view/')

            except AttributeError:
                return Response('Admin Not Present')
        return redirect('/admingui/login/')


class PendingVerification(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'pending_verification.html'

    @admin_login
    def get(self, request):
        services = Service.objects.filter(service_verify=False)
        aname = request.session.get('admin')
        return Response({'services': services, 'admin': aname})


# Admin Verification Service
class VerifyProduct(APIView):
    @admin_login
    def get(self, request, *args, **kwargs):
        service_id = kwargs.get('id')
        if service_id:
            obj = Service.objects.get(pk=service_id)
            obj.service_verify = True
            obj.save()
            return redirect('/admingui/pending-verification/')


# Admin Cancel Service
class CancelService(APIView):
    @admin_login
    def get(self, request, *args, **kwargs):
        service_id = kwargs.get('id')
        if service_id:
            obj = Service.objects.get(pk=service_id)
            obj.delete()
            return redirect('/admingui/pending-verification/')


class ServiceVerified(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'service_verified.html'

    objservice = Service.objects.filter(service_verify=True)
    @admin_login
    def get(self, request):
        aname = request.session.get('admin')
        return Response({'admin': aname, 'objservice': self.objservice})
