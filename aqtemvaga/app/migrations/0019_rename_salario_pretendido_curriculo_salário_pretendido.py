# Generated by Django 5.0.1 on 2024-11-12 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_curriculo_salario_pretendido'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curriculo',
            old_name='salario_pretendido',
            new_name='salário_pretendido',
        ),
    ]
