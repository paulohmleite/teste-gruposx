# Generated by Django 4.1 on 2022-09-02 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("empresas", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="empresa",
            name="cnpj",
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name="empresa",
            name="email",
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
    ]
