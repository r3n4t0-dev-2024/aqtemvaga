# Generated by Django 5.0.1 on 2024-11-06 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_aqtemvaga_brasil_bairro_aqtemvaga_brasil_cidade_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaga_oferecido',
            name='bairro',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
