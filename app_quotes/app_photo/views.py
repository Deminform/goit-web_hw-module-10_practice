from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'app_photo/index.html', context={'msg': 'Hello World!'})


def pictures(request):
    return render(request, 'app_photo/pictures.html', context={'pictures': 'Hello World!'})


def upload(request):
    return render(request, 'app_photo/upload.html', context={'upload': 'Hello World!'})
