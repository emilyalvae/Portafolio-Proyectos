from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProyectoForm
from .models import Proyecto
# Create your views here.

def index(request):
    return render(request, "index.html")

def proyecto(request):
    data = Proyecto.objects.all().values
    data_dict = {
        "proyectos" : data
    }
    return render(request, "proyectos.html", data_dict)

def registro_pro(request):
    data = {
        "form": ProyectoForm()
    }
    if request.method == "POST":
        form = ProyectoForm(data = request.POST, files =request.FILES)
        if form.is_valid():
            form.save()
            return redirect(to ="proyectos")
        #form = ProyectoForm()
        data["form"] = form
    return render(request, 'registro.html',data)
