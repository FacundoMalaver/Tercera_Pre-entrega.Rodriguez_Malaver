# Generated by Django 4.2.4 on 2023-08-18 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_tutores_rename_fecha_entrega_entregables_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sedes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.IntegerField(max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='tutores',
        ),
    ]