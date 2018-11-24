from . import views
from django.conf.urls import url, include

urlpatterns = [
    url(r"^$", views.index, name = "Index"),
    url(r"^registro$", views.registro, name = "registro"),
    url(r"^canciones$", views.canciones, name = "canciones"),
    url(r'^salir$',views.salir,name='salir'),
]
