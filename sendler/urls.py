from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('sends.urls', 'sends'), namespace='sends')),
    path('authh/', include(('authh.urls', 'authh'), namespace='authh')),
    path('mailings/', include(('mailings.urls', 'mailings'), namespace='mailings')),
    path('captcha/', include('captcha.urls'))

]