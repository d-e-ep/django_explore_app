from django.test import TestCase
from django.urls import path,include
from django.urls.resolvers import URLPattern
 from . views import *
# Create your tests here.

URLPattern = [
    path ('',login,name'login')
    path('register', register,name='register')
    path('otp',otp,name='otp')
]