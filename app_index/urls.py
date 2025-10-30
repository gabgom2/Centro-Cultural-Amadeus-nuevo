from django.urls import path
from .views import *


urlpatterns = [
    path("", renderizar_index, name="index"),
    path("test/", testing, name="test"),
    path("about/", about_me, name="about")
    #path("", include("estudiantes.urls"))
]
