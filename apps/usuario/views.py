from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate, login as login_auth
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User

from .forms import SignUpForm


class register(CreateView):
    model = User
    form_class = SignUpForm

    def form_valid(self, form):
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login_auth(self.request, usuario)
        return redirect('/')


def login(request):
    context = {"error": False}
    if request.method == "POST":
        user_name = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=user_name, password=password)

        if user is not None:
            login_auth(request, user)
            return redirect('listar-funciones')
        else:
            context = {'msj': 'usuario o contraseña incorrecta', 'error': True}
    return render(request, "login.html", context)


def logout(request):
    do_logout(request)
    return redirect('/')
