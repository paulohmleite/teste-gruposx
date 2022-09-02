from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ColaboradorViewSet, EmpresaViewSet

router = DefaultRouter()

router.register(r"colaboradores", ColaboradorViewSet, basename="colaboradores")
router.register(r"empresas", EmpresaViewSet, basename="empresas")

urlpatterns = router.urls
