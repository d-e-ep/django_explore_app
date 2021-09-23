from django.http.request import HttpHeaders
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import profile
import random
import http.client
from django.conf import settings


def send_otp(mobile.otp):
    conn = http.client.HTTPSConnection('api.msg91.com')
    authkey = settings.authkey
    HttpHeaders = {'content-type0': "application/json"}
    url = "http://control.msg91.com/api/sendotp.php?otp"+otp+'&sender=ABC&message=' + 'your otp is' + otp + '&mobile=' + mobile + '&authkey' = +authkey+ '&country=+91'
    conn.request("GET",url,headers=headers)
    res = conn.getresponse()
    data = res.read()
    return None

# Create your views here.



def login(request):
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')

        user = User(first_name=name)
        user.save

        otp = str(random.randint(1000,9999))
        profile = Profile(user = user , mobile=mobile)
        profile.save
        check_user = user.objects.filter(mobile = mobile).first()
        if check_user:
            context = {'message' : "'name' + register successfully"}
            return render(request , 'register.html' , context)
        send_otp = (mobile,otp)
        request.session['mobile'] = mobile
        return redirect ('otp')

    return render(request,'register.html')

def otp(request):
    mobile = request.session['mobile']
    context {mobile="mobile"}
    return render(request,'otp.html')