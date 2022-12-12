from django import forms
from .models import Proyecto

class ProyectoForm(forms.ModelForm):

    class Meta:
        model = Proyecto

        fields = ["foto", "titulo","descripcion","tags", "url_github"]

        #widgets = {
           #"foto" : forms.TextInput(attrs={"class":"form-control"}),
           #"titulo" : forms.TextInput(attrs={"class":"form-control"}),
           #"descripcion" : forms.TextInput(attrs={"class":"form-control"}),
           #"tags" : forms.TextInput(attrs={"class":"form-control"}),
           #"url_github" : forms.TextInput(attrs={"class":"form-control"}),
        #}


    
