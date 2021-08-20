from django.shortcuts import render
import random

# Create your views here.
from django.shortcuts import render
import random


def index(request):

    return render(request, 'index.html')


def password(request):
     charecter = list('abcdefghijklmnopqrstuvwxyz')

     if request.GET.get('uppercase'):
          charecter.extend(list('ABCDEFGHIJKLMOPQRSTUVWXYZ'))

     if request.GET.get('Special'):
          charecter.extend(list('!@#$%^&*()'))      

     if request.GET.get('number'):
         charecter.extend(list('0123456789'))   

     length = int(request.GET.get('length',8))

     thepassword = ''

     for x in range(length):
         thepassword += random.choice(charecter)

     return render(request, 'password.html',{'password':thepassword})
