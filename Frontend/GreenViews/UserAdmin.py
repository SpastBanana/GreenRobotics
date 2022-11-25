from django.shortcuts import render, redirect

# needed for user management
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def loginView(request):
    data = {
        'page': 'UserAdmin/login.html'
    }

    return render(request, 'index.html', data)

def registerView(request):
    data = {
        'page': 'UserAdmin/register.html'
    }

    if request.method == 'POST':
        if 'CreateNewUser' in request.POST:
            firstName = request.POST.get('firstName')
            lastName = request.POST.get('lastName')
            userName = request.POST.get('userName')
            userEmail = request.POST.get('userEmail')
            userPassword = request.POST.get('userPassword')
            print(userName)
            print(userEmail)
            print(userPassword)

            user = User.objects.create_user(f'{userName}', f'{userEmail}', f'{userPassword}')
            user.first_name = firstName
            user.last_name = lastName
            user.save()

            if userName == '' or userEmail == '' or userPassword == '':
                return redirect('/register/Error')

            else:
                return redirect('/register/Created')

        else:
            return redirect('/register')

    return render(request, 'index.html', data)

def profileView(request):
    data = {
        'page': 'UserAdmin/profile.html'
    }

    return render(request, 'index.html', data)

def logoutView(request):
    logout(request)

    return redirect('/')