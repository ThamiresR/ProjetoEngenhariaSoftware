# Generated by Django 4.1.3 on 2022-11-30 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_aluno_projeto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('horario', models.CharField(choices=[('1', '08:00 ás 09:00'), ('2', '09:00 ás 10:00'), ('3', '10:00 ás 11:00'), ('4', '13:00 ás 14:00'), ('5', '14:00 ás 15:00'), ('6', '15:00 ás 16:00'), ('7', '16:00 ás 17:00')], max_length=10)),
                ('id_aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.aluno')),
                ('id_computador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.computador')),
            ],
            options={
                'unique_together': {('horario', 'data')},
            },
        ),
    ]