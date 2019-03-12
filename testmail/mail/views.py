from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def index(request):

    send_mail('Test mail for Django by Vicky',
    'Django test mail',
    'vigneshkumar.mca2016@adhiyamaan.in',
    ['vinesh1865@gmail.com','surjithkumar.mca2016@adhiyamaan.in','mca2016b@adhiyamaan.in','manigandan.jeff@gmail.com'],
    fail_silently=False)
    return render(request, 'mail/index.html')