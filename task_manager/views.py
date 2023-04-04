from django.shortcuts import render
from django.utils.translation import gettext as _


menu = ["test!", "title", "login"]


def index(request):
    return render(request, 'index_test.html', context={
        "menu": menu,
        'tst': _('Hello World!'),
    })


def login(request):
    return render(request, 'signin.html')
