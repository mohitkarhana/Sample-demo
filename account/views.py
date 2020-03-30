from django.shortcuts import render
from django.contrib.auth.models import  User
# Create your v


def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        first_name = request.POST['password2']
        email = request.POST['email']
        user=User.objects.create_user(username=username,password=password1,last_name=last_name,first_name=first_name,email=email)
        user.save();
        print('successfully')
    return render(request,"register.html")