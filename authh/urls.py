from django.urls import path
from .views import *


urlpatterns = [
    path('login/', LoginView.as_view()  ,name='login'),
    path('registration/', Reg.as_view(), name='registration'),
    path('logout/', logout_user, name='logout'),
    path('index/', index, name='index'),

]