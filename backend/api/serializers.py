from rest_framework import serializers
from colaboradores.models import Colaborador
from empresas.models import Empresa


class ColaboradorSerializer(serializers.ModelSerializer):
    empresa =serializers.CharField(source='empresa.nome')
    user = serializers.CharField(source='user.username')
    class Meta:
        model = Colaborador
        fields = "__all__"

class EmpresaSerializer(serializers.ModelSerializer):
    # empresa =serializers.CharField(source='empresa.nome')
    # user = serializers.CharField(source='user.username')
    class Meta:
        model = Empresa
        fields = "__all__"

