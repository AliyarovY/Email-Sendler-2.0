from django.urls import path
from .views import *


urlpatterns = [
    path('', Home_Form.as_view(), name='home_form'),
    path('post_create/', post_form, name='post_form'),
]