# Generated by Django 4.1 on 2022-09-02 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("colaboradores", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="colaborador",
            name="cnpj",
        ),
    ]