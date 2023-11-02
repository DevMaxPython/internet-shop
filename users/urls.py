from django.urls import path
from .views import sign_in, sign_up, logout, profile, change_password

app_name = 'users'

urlpatterns = [
    path('sign_in/', sign_in, name='sign_in'),
    path('sign_up/', sign_up, name='sign_up'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('change_password/', change_password, name='change_password'),
]

