from django.urls import path
from . import views
from .views import registrar_user
urlpatterns = [
    path('registrar/',registrar_user,name = "registrar"),
]