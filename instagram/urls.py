from django.contrib.auth.validators import UnicodeUsernameValidator
from django.urls import path, re_path

from instagram.views import post_new, post_detail, user_page, index, post_like, post_unlike

app_name = 'instagram'

# UnicodeUsernameValidator.regex

urlpatterns = [
    path('', index, name='index'),
    path('post/new/', post_new, name='post_new'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/<int:pk>/like/', post_like, name='post_like'),
    path('post/<int:pk>/unlike/', post_unlike, name='post_unlike'),
    re_path(r'^(?P<username>[\w.@+-]+)/$', user_page, name='user_page'),

]