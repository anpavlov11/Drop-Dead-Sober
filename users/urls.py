from django.urls import path

from.views import signup

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', log_in, name='login'),
]