# Generated by Django 5.0.2 on 2024-05-25 20:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gecopf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='concept',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='transaction',
            name='cantidad',
            field=models.DecimalField(decimal_places=2, default=0.0, help_text='Ingrese la cantidad en euros', max_digits=10),
        ),
        migrations.AddField(
            model_name='transaction',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='concept',
            name='detalle',
            field=models.TextField(blank=True, help_text='Ingrese una breve descripción del concepto', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='concept',
            name='tipo',
            field=models.CharField(choices=[('Ingreso', 'Ingreso'), ('Gasto', 'Gasto'), ('Inversión', 'Inversión')], help_text='Ingrese el tipo del concepto', max_length=10),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='concepto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gecopf.concept'),
        ),
    ]
