# Generated by Django 3.0.8 on 2020-07-08 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cidades', '0009_auto_20200708_1842'),
        ('feriados', '0005_auto_20200708_1840'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FeridoEstadual',
            new_name='FeriadoEstadual',
        ),
        migrations.AlterField(
            model_name='feriadoestadual',
            name='uf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cidades.Uf'),
        ),
    ]