from django.shortcuts import render

menu = ["test!", "title", "login"]


def index(request):
    return render(request, 'index_test.html', context={
        "menu": menu,
        'tst': 'TEST',
    })


def login(request):
    return render(request, 'signin.html')
