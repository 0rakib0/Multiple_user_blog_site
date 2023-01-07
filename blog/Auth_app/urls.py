from django.urls import path
from . import views

app_name = 'Auth_app'

urlpatterns = [
    path('Rejistration/', views.Registration, name='rejistration'),
    path('Login/', views.Login_form, name='login'),
    path('Do-login/', views.Do_login, name='do_login'),
    path('do-logut/', views.Do_logout, name='logout'),
    path('user/profile/', views.Profile, name='profile'),
    path('Edit/profile/<str:id>/', views.Edit_profle, name='edit_profile'),
    path('update/profile/', views.Update_profile, name='update_profile')
]