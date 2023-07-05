from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def logIn(request):
    if request.method == "POST":
        if "guest" in request.POST:
            return redirect('/home/')
        else:
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request,username=username, password = password )
            if user is not None:
                login(request, user)
                return redirect('/home/')
            else:
                messages.success(request, ("Error de autenticación"))
                return redirect('logIn')
    else:
        if request.user.is_authenticated:
            return redirect('/home/')
        else:
            return render(request, 'login.html')
