from django.contrib.auth.views import PasswordChangeView
from django.urls import path, re_path

from accounts.views import signup, login, logout, profile_edit, password_change, user_follow, user_unfollow

app_name = 'accounts'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('edit/', profile_edit, name='profile_edit'),
    path('password_change/', password_change, name='password_change'),
    re_path(r'^(?P<username>[\w.@+-]+)/follow/$', user_follow, name='user_follow'),
    re_path(r'^(?P<username>[\w.@+-]+)/unfollow/$', user_unfollow, name='user_unfollow'),

    # path()

]