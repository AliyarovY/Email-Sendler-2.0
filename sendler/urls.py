from django.contrib import admin
from django.urls import path, include
from mailings.views import page_not_found


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('sends.urls', 'sends'), namespace='sends')),
    path('authh/', include(('authh.urls', 'authh'), namespace='authh')),
    path('mailings/', include(('mailings.urls', 'mailings'), namespace='mailings')),
    path('captcha/', include('captcha.urls'))

]

handler404 = page_not_found