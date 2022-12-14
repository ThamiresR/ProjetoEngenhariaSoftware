# Generated by Django 4.1.3 on 2022-11-30 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240, verbose_name='Name')),
                ('email', models.EmailField(max_length=254)),
                ('login', models.CharField(max_length=240, verbose_name='Login')),
                ('senha', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=240, verbose_name='Titulo')),
                ('descricao', models.CharField(max_length=240, verbose_name='Descriccao')),
                ('dataInicio', models.DateField()),
                ('dataFim', models.DateField()),
                ('coordenador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.coordenador')),
            ],
        ),
    ]
