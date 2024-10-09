from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages

from .forms import RegisterForm, LoginForm


# Create your views here.
class RegisterView(View):
    template_name = 'app_auth/register.html'
    form_class = RegisterForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')  # TODO Check if ".get" is needed
            messages.success(request, f'Greeting {username}, your account has been created.')
            return redirect(to='app_auth:signin')
        return render(request, self.template_name, {'form': form})
