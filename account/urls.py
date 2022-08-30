from django.urls import path

from .views import LoginAPI, MeView, get_all_user_list,ClassList,StudentsList
from knox.urls import views as knoxviews
from . import views



urlpatterns = [
    path('log-in/',LoginAPI.as_view() ,name='log-in'),
    path('log-out/',knoxviews.LogoutView.as_view() ,name='log-out'),
    path('me/', MeView.as_view(), name='me'),
    path('users/list', get_all_user_list), 
    # path('school/list',),
    path('class/list',ClassList.as_view(),name='classes'),
    path('students/list',StudentsList.as_view(),name='students')

    # path('',views.index,name='index'),
    
]
