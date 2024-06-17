# Generated by Django 5.0.2 on 2024-06-06 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gecopf', '0006_alter_customuser_fecha_de_nacimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='genero',
            field=models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('N', 'No Binario')], default='', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='fecha_de_nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
    ]