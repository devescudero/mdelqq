# Generated by Django 5.0.2 on 2024-06-06 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gecopf', '0008_alter_customuser_imagen_de_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='imagen_de_perfil',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]