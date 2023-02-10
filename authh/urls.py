
from django.urls import path
from .views import *


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('registration/', email_verify, name='registration'),
    path('logout/', logout_user, name='logout'),
    path('index/', index, name='index'),
    path('post_reg/', reg, name='post_reg'),

]

                      