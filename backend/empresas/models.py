# from django.db import models

# from django.db import models
# from django_cpf_cnpj.fields import CPFField, CNPJField
# from phonenumber_field.modelfields import PhoneNumberField

# # from django.contrib.auth.User import User


# # Create your models here.
# class Empresa(models.Model):
#     # codigo = models.CharField(null=True, blank=True, max_length=20)
#     # cpf = CPFField(masked=True)  # To enable auto-mask xxx.xxx.xxx-xx
#     cnpj = CNPJField(masked=False)
#     # user = models.ForeignKey(User, on_delete=models.CASCADE)
#     email = models.EmailField(max_length=50, null=False, blank=False)
#     telefone = PhoneNumberField(unique=True, null=False, blank=False)
#     endereco1 = models.CharField(max_length=50, null=True, blank=True)
#     endereco2 = models.CharField(max_length=50, null=True, blank=True)
