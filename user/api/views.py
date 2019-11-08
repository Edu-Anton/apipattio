from django.shortcuts import render
from rest_framework import viewsets,permissions,authentication
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from django.http import HttpResponse
from rest_framework.authtoken.models import Token
import json
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class RegistroUsuario(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    def post(self,request,*arg,**kwargs):
        #Creando el Nuevo Usuario
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
       

        user = User.objects.create_user(username,email,password)
        user.save()
        token = Token.objects.create(user=user)
        data = {'Token':token.key}
        dump = json.dumps(data)
        return HttpResponse(dump,content_type='application/json')