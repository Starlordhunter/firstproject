from django.urls import path

from .views import LoginAPI, MeView, get_all_user_list
from knox.urls import views as knoxviews


urlpatterns = [
    
    path('log-in/',LoginAPI.as_view() ,name='log-in'),
    path('log-out/',knoxviews.LogoutView.as_view() ,name='log-out'),
    path('me/', MeView.as_view(), name='me'),
    path('users/', get_all_user_list), 
    
]