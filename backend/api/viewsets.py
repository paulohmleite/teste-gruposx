from django.shortcuts import get_object_or_404
from .serializers import ColaboradorSerializer, EmpresaSerializer
from rest_framework import viewsets, status
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from colaboradores.models import Colaborador
from empresas.models import Empresa



class ColaboradorViewSet(viewsets.ModelViewSet):
    """
    Viewset para listar colaboradores e tornar possível um CRUD no modelo.
    """

    serializer_class = ColaboradorSerializer
    queryset = Colaborador.objects.all()

    def list(self, request):
        queryset = Colaborador.objects.all()
        serializer = ColaboradorSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Colaborador.objects.all()
        colaborador = get_object_or_404(queryset, pk=pk)
        serializer = ColaboradorSerializer(colaborador)
        return Response(serializer.data)


class EmpresaViewSet(viewsets.ModelViewSet):
    """
    Viewset para listar empresas e tornar possível um CRUD no modelo.
    """

    serializer_class = EmpresaSerializer
    # queryset = Empresa.objects.all()

    def get_queryset(self):
        result = Empresa.objects.all()
        return result

    def list(self, request):
        queryset = Empresa.objects.all()
        serializer = EmpresaSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Empresa.objects.all()
        colaborador = get_object_or_404(queryset, pk=pk)
        serializer = EmpresaSerializer(colaborador)
        return Response(serializer.data)

    
