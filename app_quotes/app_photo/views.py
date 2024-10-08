from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'app_photo/index.html', context={'msg': 'Hello World!'})
