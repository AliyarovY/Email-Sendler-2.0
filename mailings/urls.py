from django.urls import path
from .views import *


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('update/<int:pk>/', UpdateMailing.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteMailing.as_view(), name='delete'),
    path('users/', Users.as_view(), name='users')

]

