from django.urls import path

from .views import LoginAPI, MeView, get_all_user_list,ClassInfo
from knox.urls import views as knoxviews
from . import views



urlpatterns = [
    path('log-in/',LoginAPI.as_view() ,name='log-in'),
    path('log-out/',knoxviews.LogoutView.as_view() ,name='log-out'),
    path('me/', MeView.as_view(), name='me'),
    path('users/', get_all_user_list), 
    path('teacher/',ClassInfo.as_view(),name='classInfo')

    # path('',views.index,name='index'),
    
]
