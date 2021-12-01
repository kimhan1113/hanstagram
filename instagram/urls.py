from django.urls import path

from instagram.views import post_new

app_name = 'instagram'

urlpatterns = [
    path('post/new/', post_new, name='post_new'),
]