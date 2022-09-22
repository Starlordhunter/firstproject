from django.urls import path

from .views import LoginAPI, MeView, MyTokenObtainPairView, get_all_user_list,ClassList,StudentsList,SchoolList,TeacherList,PrincipalList
from knox.urls import views as knoxviews
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)



urlpatterns = [
    path('log-in/',LoginAPI.as_view() ,name='log-in'),
    path('log-out/',knoxviews.LogoutView.as_view() ,name='log-out'),
    path('me/', MeView.as_view(), name='me'),
    path('users/list/', get_all_user_list), 
    path('school/list/',SchoolList.as_view(),name='school'),
    path('class/list/',ClassList.as_view(),name='classes'),
    path('teacher/list/',TeacherList.as_view(),name='teachers'),
    path('students/list/',StudentsList.as_view(),name='students'),
    path('principal/list/',PrincipalList.as_view(),name='principal'),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),


    # path('',views.index,name='index'),
    
]