from django.shortcuts import redirect, render
from .forms import PicturesForm
from .models import Pictures
# Create your views here.


def index(request):
    return render(request, 'app_photo/index.html', context={'msg': 'Hello World!'})


def pictures(request):
    pics = Pictures.objects.all()
    return render(request, 'app_photo/pictures.html', context={'pics': pics})


def upload(request):
    form = PicturesForm(instance=Pictures())
    if request.method == 'POST':
        form = PicturesForm(request.POST, request.FILES, instance=Pictures())
        if form.is_valid():
            form.save()
            return redirect(to='app_photo:pictures')
    return render(request, 'app_photo/upload.html', context={'form': form})
