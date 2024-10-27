from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, LivroViewSet, MensagemViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'livros', LivroViewSet)
router.register(r'mensagens', MensagemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
