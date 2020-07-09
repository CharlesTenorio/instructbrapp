# Generated by Django 3.0.8 on 2020-07-08 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cidades', '0011_auto_20200708_2125'),
        ('feriados', '0007_auto_20200708_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feriadoestadual',
            name='uf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cidades.Uf'),
        ),
        migrations.AlterUniqueTogether(
            name='feriadoestadual',
            unique_together={('uf', 'data_feriado')},
        ),
        migrations.AlterUniqueTogether(
            name='feriadomunicipal',
            unique_together={('cidade', 'data_feriado')},
        ),
        migrations.RemoveField(
            model_name='feriadoestadual',
            name='codigo',
        ),
        migrations.RemoveField(
            model_name='feriadomunicipal',
            name='codigo',
        ),
    ]