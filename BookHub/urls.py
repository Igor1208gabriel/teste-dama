from django.urls import include, path
from .views import Teste

urlpatterns = [
    path('', Teste.as_view()),
]