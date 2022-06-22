from django.contrib import admin
from django.urls import path
from Twitter.views import deletePost, edit_profile, follow, primeraVista, profile, register, unfollow
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', primeraVista, name = 'Home'),
    path('register/', register, name = 'Register'),
    path('login/', LoginView.as_view(template_name = 'login.html'), name = 'Login'),
    path('logout/', LogoutView.as_view(), name = 'Logout'),
    path('delete/<int:post_id>', deletePost, name ='Delete Post'),
    path('profileDetail/<str:username>/', profile, name = 'Profile Details'),
    path('editProfile/', edit_profile, name = 'Edit Profile'),
    path('follow/<str:username>/', follow, name = 'Follow'),
    path('unfollow/<str:username>/', unfollow, name = 'Unfollow'),
    
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
