# Generated by Django 3.0.8 on 2020-07-08 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cidades', '0005_auto_20200708_1800'),
        ('feriados', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FeriadosMuncipais',
            new_name='FeriadoMunicipal',
        ),
        migrations.AlterField(
            model_name='feraidoestadual',
            name='uf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cidades.Uf'),
        ),
    ]
