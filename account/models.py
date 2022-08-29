from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
import datetime

# from core.models import School

# Create your CustomUserManager here.
class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, mobile, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError('Password is not provided')

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            mobile = mobile,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, first_name, last_name, mobile, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email, password, first_name, last_name, mobile, password, **extra_fields)

    def create_superuser(self, email, password, first_name, last_name, mobile, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(email, password, first_name, last_name, mobile, **extra_fields)

# Create your User Model here.
class User(AbstractBaseUser,PermissionsMixin):
    # Abstractbaseuser has password, last_login, is_active by default

    email = models.EmailField(db_index=True, unique=True, max_length=254)
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=50)
    address = models.CharField( max_length=250)

    is_staff = models.BooleanField(default=True) # must needed, otherwise you won't be able to loginto django-admin.
    is_active = models.BooleanField(default=True) # must needed, otherwise you won't be able to loginto django-admin.
    is_superuser = models.BooleanField(default=False) # this field we inherit from PermissionsMixin.

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','mobile']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'



class Profile(models.Model):
    image = models.ImageField(upload_to="profile" ,blank = True)
    gender = models.CharField(max_length = 112)
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    dob = models.CharField(max_length=10)
    age = models.CharField(max_length=20)
    role = models.CharField(max_length=50)        
    created_at = models.DateTimeField(editable=False ,null = True)
    updated_at = models.DateTimeField(null = True)

    def __str__(self):
        return self.user.email

class School(models.Model):
    school_name = models.CharField(max_length=50)
    school_info = models.CharField(max_length=100)
    school_branch_info = models.CharField(max_length=50)
    school_tel_no = models.CharField(max_length=12)

    def __str__(self):
        return self.school_name



class Teacher(models.Model):
    teacher_name = models.CharField(max_length=20)
    teacher_tel_no = models.CharField(max_length=12)
    teacher_address = models.CharField(max_length=50)

    classes = models.ManyToManyField('Classes', related_name="classes")
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.teacher_name

class Student(models.Model):
    student_name = models.CharField(max_length=20)
    student_tel_no = models.CharField(max_length=12)
    student_address = models.CharField(max_length=50)
    
    classes = models.ForeignKey('Classes',on_delete=models.CASCADE)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name


class Classes(models.Model):
    class_name = models.CharField(max_length=20)
    class_rank = models.CharField(max_length=100)

    school = models.ForeignKey(School,on_delete=models.CASCADE)

    def count_of_students(self):
        return Student.objects.filter(classes_id=self).count()
    
    def student_in_classes(self):
        return list(Student.objects.filter(classes_id=self))

    def __str__(self):
        return self.class_name
    
