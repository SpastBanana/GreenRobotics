from django.shortcuts import render

def homeView(request):
    data = {
        'page': 'home.html'
    }

    return render(request, 'index.html', data)