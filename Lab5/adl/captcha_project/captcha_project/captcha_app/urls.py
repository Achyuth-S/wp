from django.shortcuts import redirect
from django.urls import path
from .views import captcha_view

urlpatterns = [
    path('captcha/', captcha_view, name='captcha'),
     path('', lambda request: redirect('captcha'), name='home'),

]
