# Generated by Django 5.0.1 on 2024-11-12 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_rename_salario_pretendido_curriculo_salário_pretendido'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curriculo',
            old_name='cargo',
            new_name='cargo_pretendido',
        ),
    ]
