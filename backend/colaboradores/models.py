# from django.db import models

# from django.db import models

# from django.db import models
# from django_cpf_cnpj.fields import CPFField, CNPJField
# from phonenumber_field.modelfields import PhoneNumberField
# from contas.models import User

# from empresas.models import Empresa


# # Create your models here.
# class Colaborador(models.Model):
#     # codigo = models.CharField(null=True, blank=True, max_length=20)
#     cpf = CPFField(masked=True)  # To enable auto-mask xxx.xxx.xxx-xx
#     cnpj = CNPJField(masked=False)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     email = models.EmailField(max_length=50, null=False, blank=False)
#     telefone = PhoneNumberField(unique=True, null=False, blank=False)
#     endereco1 = models.CharField(max_length=50, null=True, blank=True)
#     endereco2 = models.CharField(max_length=50, null=True, blank=True)
#     empresa = models.ForeignKey(
#         Empresa, on_delete=models.CASCADE, null=False, blank=False
#     )
