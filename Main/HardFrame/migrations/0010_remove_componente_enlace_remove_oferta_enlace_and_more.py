# Generated by Django 4.2.2 on 2023-07-10 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HardFrame', '0009_alter_componente_id_produc_alter_oferta_id_produc_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='componente',
            name='enlace',
        ),
        migrations.RemoveField(
            model_name='oferta',
            name='enlace',
        ),
        migrations.RemoveField(
            model_name='periferico',
            name='enlace',
        ),
        migrations.RemoveField(
            model_name='software',
            name='enlace',
        ),
    ]
