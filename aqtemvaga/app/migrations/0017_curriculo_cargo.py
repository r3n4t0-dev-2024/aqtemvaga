# Generated by Django 5.0.1 on 2024-11-12 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_visualizacaocurriculo_visualizacoes_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='curriculo',
            name='cargo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
