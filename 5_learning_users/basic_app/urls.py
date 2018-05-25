from django.urls import path
from basic_app import views

#for template urls
app_name = 'basic_app'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('login/', views.user_login, name='login'),
]