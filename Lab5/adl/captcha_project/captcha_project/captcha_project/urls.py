from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha_app.urls')),  # Your captcha app URL
    path('', lambda request: redirect('captcha/')),  # Redirect root URL to captcha
]
