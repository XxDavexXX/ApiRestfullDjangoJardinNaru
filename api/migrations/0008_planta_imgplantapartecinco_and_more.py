# Generated by Django 5.0 on 2024-01-29 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_planta_dificultad_planta_lugara_planta_lugarb_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='planta',
            name='imgplantapartecinco',
            field=models.CharField(default='imgs/imgplantapartecinco.jpeg', max_length=255),
        ),
        migrations.AddField(
            model_name='planta',
            name='imgplantapartecuatro',
            field=models.CharField(default='imgs/imgplantapartecuatro.jpeg', max_length=255),
        ),
        migrations.AddField(
            model_name='planta',
            name='imgplantapartedos',
            field=models.CharField(default='imgs/imgplantapartedos.jpeg', max_length=255),
        ),
        migrations.AddField(
            model_name='planta',
            name='imgplantaparteseis',
            field=models.CharField(default='imgs/imgplantaparteseis.jpeg', max_length=255),
        ),
        migrations.AddField(
            model_name='planta',
            name='imgplantapartetres',
            field=models.CharField(default='imgs/imgplantapartetres.jpeg', max_length=255),
        ),
        migrations.AddField(
            model_name='planta',
            name='imgplantaparteuno',
            field=models.CharField(default='imgs/imgplantaparteuno.jpeg', max_length=255),
        ),
    ]
