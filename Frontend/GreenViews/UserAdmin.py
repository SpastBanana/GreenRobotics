from django.shortcuts import render, redirect
from .UserAdminPrev import getPageInfo

# needed for user management
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def loginView(request):
    if request.user.is_authenticated:
        return redirect('/profile')

    data = {
        'page': 'UserAdmin/login.html'
    }

    if request.method == 'POST':
        if 'LoginUser' in request.POST:
            userName = request.POST.get('userName')
            userPassword = request.POST.get('userPassword')
            user = authenticate(username=userName, password=userPassword)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'index.html', {'page': 'UserAdmin/login.html', 'error': 'Your username and/or password were incorrect.'})
        else:
            return redirect('/login')


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

            user = User.objects.create_user(f'{userName}', f'{userEmail}', f'{userPassword}')
            user.first_name = firstName
            user.last_name = lastName
            user.save()

            if userName == '' or userEmail == '' or userPassword == '':
                data = {
                    'page': 'UserAdmin/register.html',
                    'check': 'none',
                    'error': 'No data in required fields'
                }
                return render(request, 'index.html', data)

            else:
                data = {
                    'page': 'UserAdmin/register.html',
                    'check': 'User created, ask the system admin for system rights',
                    'error': 'none'
                }
                return render(request, 'index.html', data)

        else:
            return redirect('/register')

    return render(request, 'index.html', data)

def profileView(request):
    userName = request.user.username
    perms = request.user.get_all_permissions()

    data = getPageInfo(userName, perms)

    return render(request, 'index.html', data)

def logoutView(request):
    logout(request)

    return redirect('/')