from django.urls import path
from. import views

app_name = 'Blog_app'

urlpatterns = [
    path('creat/blog/', views.Blog_create, name='create_blog'),
    path('details/blog/<str:slug>/', views.Blog_details, name='blog_details'),
    path('Edit/blog/<str:id>/', views.Edit_blog, name='edit_blog'),
    path('Update/blog/', views.Update_blog, name='update_blog'),
]
