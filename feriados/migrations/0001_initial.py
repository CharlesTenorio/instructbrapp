# Generated by Django 3.0.8 on 2020-07-08 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cidades', '0004_auto_20200708_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeriadosMuncipais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_feriado', models.CharField(max_length=150)),
                ('data_feriado', models.DateField()),
                ('mes_dia', models.CharField(max_length=5)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cidades.Cidade')),
            ],
        ),
        migrations.CreateModel(
            name='FeraidoEstadual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=2)),
                ('nome_feriado', models.CharField(max_length=150)),
                ('data_feriado', models.DateField()),
                ('mes_dia', models.CharField(blank=True, max_length=5, null=True)),
                ('uf', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cidades.Uf')),
            ],
        ),
    ]
