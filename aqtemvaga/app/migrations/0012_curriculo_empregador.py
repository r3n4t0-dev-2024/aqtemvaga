# Generated by Django 5.0.1 on 2024-11-08 23:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_empregador_primeiro_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='curriculo',
            name='empregador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.empregador'),
        ),
    ]