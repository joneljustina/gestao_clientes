from django.urls import path
from .views import home
from .views import sair

urlpatterns = [
    path('', home, name="home"),
    path('logout/', sair, name="logout"),
]
