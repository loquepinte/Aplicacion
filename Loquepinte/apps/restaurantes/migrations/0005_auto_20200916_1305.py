# Generated by Django 3.1 on 2020-09-16 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantes', '0004_comentario_valoracion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='valoracion',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]