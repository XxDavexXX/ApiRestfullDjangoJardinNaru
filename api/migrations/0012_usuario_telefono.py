# Generated by Django 5.0 on 2024-02-06 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_usuario_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='telefono',
            field=models.CharField(default='', max_length=255),
        ),
    ]
