# Generated by Django 4.1 on 2022-09-02 19:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("colaboradores", "0004_alter_colaborador_cpf"),
    ]

    operations = [
        migrations.AlterField(
            model_name="colaborador",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
