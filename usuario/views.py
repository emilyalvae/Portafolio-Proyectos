from django.shortcuts import render,redirect
from .forms import RegistroUsuario
from django.contrib.auth import authenticate, login
from django.contrib import messages
from portafolio.views import index
# Create your views here.
def registrar_user(request):
    data = { 
        "form": RegistroUsuario()
    }
    if request.method == 'POST':
        registro = RegistroUsuario(data = request.POST)
        if registro.is_valid():
            registro.save()
            user = authenticate(username = registro.cleaned_data["username"],
             password=registro.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has resgistrado correctamente")
            return redirect(to="index")
        data["form"] = registro
    return render(request,"registrar.html", data)

