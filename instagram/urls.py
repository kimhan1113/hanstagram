from django.contrib.auth.validators import UnicodeUsernameValidator
from django.urls import path, re_path

from instagram.views import post_new, post_detail, user_page

app_name = 'instagram'

# UnicodeUsernameValidator.regex

urlpatterns = [
    path('post/new/', post_new, name='post_new'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    re_path(r'^(?P<username>[\w.@+-]+)/$', user_page, name='user_page'),

]