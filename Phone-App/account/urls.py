from django.urls import *
from .import views
urlpatterns = [
    path('Create/New/User/Page',views.createuser,name='create-user'),
    path('User/Login/page',views.user_login,name='login'),
    path('User/Logout/Page',views.user_logout,name='user-logout'),
]
