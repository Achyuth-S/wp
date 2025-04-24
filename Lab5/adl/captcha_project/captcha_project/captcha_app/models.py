from django.db import models
from django.utils import timezone

class CaptchaEntry(models.Model):
    captcha_text = models.CharField(max_length=6)
    created_at = models.DateTimeField(default=timezone.now)
    is_valid = models.BooleanField(default=True)  # You can use this to invalidate on expiry or match