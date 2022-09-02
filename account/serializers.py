from asyncio.windows_events import NULL
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate

# from core.serializers import StaffSerializer
from .models import Classes, School, Student, Subject, Teacher, User, Profile


#ProfileSerializer
class ProfileSerializer(serializers.ModelSerializer):
    image_path = serializers.SerializerMethodField()
    school_info = serializers.SerializerMethodField()
    school_branch_info = serializers.SerializerMethodField()    
    class Meta:
        model = Profile
        fields = ['user', 'dob', 'role', 'image' ,'gender' ,'image_path' ,'id']
        extra_kwargs = {
            'image': {
                'write_only' : True,
            }
        }
    
    def get_image_path(self ,obj):
        return obj.image.url

    
        

#userInfoSerializer
class GetUserSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()
    
    def get_profile(self ,obj):
        try :
            profile = obj
            return ProfileSerializer(profile).data
        except :
            return None

    class Meta:
        model = User 
        fields = ['id', 'email', 'first_name', 'last_name', 
        'is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions', 'profile']

    

class UserSerializer(serializers.ModelSerializer): 
    
    profile = serializers.SerializerMethodField()
    
    def get_profile(self ,obj):
        try :
            profile = Profile.objects.get(profile_user__in=obj)
            print(profile)
            return ProfileSerializer(profile).data
        except :
            return None
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 
        'is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions', 'profile']

#login serializer
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self ,data):
        user = authenticate(**data)
        if not user:
            raise serializers.ValidationError("email or password Incorrect")
        
        return data 

#SchoolSerializer
class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

#SubjectSerializer
class SubjectSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(max_length=20)
    class Meta:
        model = Subject
        fields = ['subject_name']

#StudentSerializer
class StudentSerializer(serializers.ModelSerializer):
    
    student_name = serializers.CharField(max_length=100)
    student_tel_no = serializers.CharField(max_length=100)
    subject_taken = SubjectSerializer(many=True)
    class Meta:
        model = Student
        fields = ['id', 'student_name','student_tel_no','student_address','classes_id','user_id','subject_taken']

#ClassesSerializer
class ClassesSerializer(serializers.ModelSerializer):
    count_of_students = serializers.IntegerField()
    class_name = serializers.CharField(max_length=100)
    student_in_classes = StudentSerializer(many=True)
    


    class Meta:
        model = Classes
        fields = ['class_name','count_of_students','student_in_classes']
    


#TeacherSerializer
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

#PrincipalSerializer
class PrincipalSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

#PrincipalListSerializer
class PrincipalListSerializer(serializers.ModelSerializer):
    count_of_students = serializers.IntegerField()
    class_name = serializers.CharField(max_length=100)
    student_in_classes = StudentSerializer(many=True)
    teacher_info = TeacherSerializer(many=True)
    


    class Meta:
        model = Classes
        fields = ['teacher_info','class_name','count_of_students','student_in_classes']
