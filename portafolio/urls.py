from django.urls import path
from . import views
from .views import index, registro_pro, proyecto

urlpatterns = [
    path('',index, name ="index" ),
    path('registro/', registro_pro, name = "registro"),
    path('proyectos/', proyecto, name = "proyectos"),
]