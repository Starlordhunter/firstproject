from django.contrib import admin

# Register your models here.

from account.models import Profile, User,School,Classes,Teacher,Student

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(School)
admin.site.register(Classes)
admin.site.register(Teacher)
admin.site.register(Student)