# Generated by Django 5.0.1 on 2024-11-08 23:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_curriculo_empregador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curriculo',
            name='empregador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='curriculos', to='app.empregador'),
        ),
    ]
