# Generated by Django 3.1 on 2020-09-16 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantes', '0003_auto_20200915_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='valoracion',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
