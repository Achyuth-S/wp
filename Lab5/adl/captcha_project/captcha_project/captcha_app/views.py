import random
import string
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.contrib import messages
from .models import CaptchaEntry

def generate_captcha():
    """Generate a random captcha text."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def captcha_view(request):
    if request.method == 'POST':
        # Get user input and stored CAPTCHA
        user_input = request.POST.get('captcha')
        captcha_answer = request.session.get('captcha_answer')

        # Check if the answer matches
        if user_input == captcha_answer:
            return JsonResponse({'message': 'CAPTCHA Matched!'}, status=200)
        else:
            # Increment failed attempts counter
            attempts = request.session.get('captcha_attempts', 0)
            attempts += 1
            request.session['captcha_attempts'] = attempts

            if attempts >= 3:
                return JsonResponse({'message': 'Too many failed attempts! The CAPTCHA input is now disabled.'}, status=400)
            return JsonResponse({'message': 'CAPTCHA mismatch! Try again.'}, status=400)

    # Generate a new CAPTCHA and save it in the session
    captcha_text = generate_captcha()
    request.session['captcha_answer'] = captcha_text
    request.session['captcha_attempts'] = 0  # Reset attempts

    CaptchaEntry.objects.create(captcha_text=captcha_text)

    return render(request, 'captcha_app/captcha.html', {'captcha_text': captcha_text})
