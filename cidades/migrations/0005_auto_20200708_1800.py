# Generated by Django 3.0.8 on 2020-07-08 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cidades', '0004_auto_20200708_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cidade',
            name='codito_uf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cidades.Uf'),
        ),
    ]