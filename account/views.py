from json import JSONDecoder
import json
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from account.models import Profile, School, SchoolBranch, User

from .serializers import GetUserSerializer, LoginSerializer, SchoolSerializer, UserSerializer
from knox.models import AuthToken
from django.db.models import OuterRef, Subquery, Q


class LoginAPI(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self ,request , *args ,**kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['email']
        user = User.objects.get(email=username)

        return Response({
            'user' : GetUserSerializer(user).data,
            'token' : AuthToken.objects.create(user)[1]
        })

class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = GetUserSerializer(request.user)        
        return Response({
            'user' : serializer.data,            
        })



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

