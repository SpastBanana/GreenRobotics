# Django import
from django.shortcuts import render, redirect

# Standard first view of the site
def homeView(request):
    data = {
        'page': 'home.html'
    }

    return render(request, 'index.html', data)

def deletepostView (request, page):
    return redirect(f'{page}')