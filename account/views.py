from json import JSONDecoder
import json
from multiprocessing import context
from pydoc import classname
from urllib import request
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django.http import HttpResponse
from django.contrib.auth import login
from account.models import Profile, School, User,Student,Teacher,Classes

from rest_framework.authtoken.serializers import AuthTokenSerializer
from .serializers import GetUserSerializer, LoginSerializer, SchoolSerializer, UserSerializer,StudentSerializer,ClassesSerializer,TeacherSerializer
from knox.models import AuthToken
from knox.auth import TokenAuthentication
from django.db.models import OuterRef, Subquery, Q

from django.shortcuts import redirect




class LoginAPI(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self ,request , *args ,**kwargs):
        
        serializer = AuthTokenSerializer(data=request.data)
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['email']
        user = User.objects.get(email=username)
        login(request,user)

        return Response({
            'user' : GetUserSerializer(user).data,
            'token' : AuthToken.objects.create(user)[1]
        })

class MeView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        serializer = GetUserSerializer(request.user)        
        return Response({
            'user' : serializer.data,            
        })

class ClassList(APIView):
    
    def get(self, request):
        if request.user.is_superuser:
            class_info = Student.objects.all()
            serializer = StudentSerializer(class_info, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return redirect('log-in')

class StudentsList(APIView):
    class_choice = '1 Anugerah'
    

    def get(self, request):
        teacher = Teacher.objects.filter(user=self.request.user)
        if teacher:
            class_info = Classes.objects.filter(classes__in=teacher)   
            # print(class_info)
            serializer = ClassesSerializer(class_info, many=True)
            # print(serializer)
            return JsonResponse(serializer.data, safe=False)
        else:
            return redirect('log-in')


@api_view(['GET'])
def get_all_user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def post_create_staff_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
       serializer.save()     
       return Response(serializer.data, status=status.HTTP_201_CREATED)


