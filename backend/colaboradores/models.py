from django.db import models

from django.db import models

from django.db import models
from django_cpf_cnpj.fields import CPFField, CNPJField
from phonenumber_field.modelfields import PhoneNumberField
from contas.models import User

from empresas.models import Empresa


# Create your models here.
class Colaborador(models.Model):
    primeiro_nome = models.CharField(max_length=30, null=False, blank=False)
    ultimo_nome = models.CharField(max_length=30, null=True, blank=True)
    # codigo = models.CharField(null=True, blank=True, max_length=20)
    # cpf = CPFField(masked=True,)  # To enable auto-mask xxx.xxx.xxx-xx
    cpf = models.CharField(max_length=11, null=True, blank=True)
    # cnpj = CNPJField(masked=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    email = models.EmailField(max_length=50, null=True, blank=True)
    # telefone = PhoneNumberField(unique=True, null=True, blank=True)
    telefone = models.CharField(max_length=12, null=True, blank=True)
    endereco1 = models.CharField(max_length=50, null=True, blank=True, verbose_name="Linha 1")
    endereco2 = models.CharField(max_length=50, null=True, blank=True, verbose_name="Linha 2")
    empresa = models.ForeignKey(
        Empresa, on_delete=models.CASCADE, null=False, blank=False,
    )

    def __str__(self):
        return self.user.username
