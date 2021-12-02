from django.urls import path

from instagram.views import post_new, post_detail

app_name = 'instagram'

urlpatterns = [
    path('post/new/', post_new, name='post_new'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
]