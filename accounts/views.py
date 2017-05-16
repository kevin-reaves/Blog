from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def signup(request):
    if request.method == "POST":
        pword = request.POST["password1"]
        password2 = request.POST["password2"]
        uname = request.POST["username"]
        emailaddr = request.POST["email"]

        if pword == password2:
            try:
                user = User.objects.get(username = uname)
                return render(request, 'accounts/signup.html', {'error': "This username has already been taken"})
            except User.DoesNotExist:
                user = User.objects.create_user(username = uname, email = emailaddr, password = pword)
                login(request, user)

                return render(request, 'accounts/signup.html')
        else:
            return render(request, 'accounts/signup.html', {'error': "The passwords didn't match"})
    else:
        return render(request, 'accounts/signup.html')