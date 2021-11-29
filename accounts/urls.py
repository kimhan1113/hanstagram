from django.urls import path

from accounts.views import signup, login, logout, profile_edit

app_name = 'accounts'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('edit/', profile_edit, name='profile_edit'),
    # path('verify/<str:key>', complete_verification),
]