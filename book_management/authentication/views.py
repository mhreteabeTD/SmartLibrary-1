from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            if user.is_staff or user.is_superuser:
                return redirect('books/')
            else:
                return redirect('bookfinder/')
        else:
            pass
            #handle login error
        
    return render(request,'login.html')