# Generated by Django 2.1.7 on 2019-08-29 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canchas', '0002_auto_20190829_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancha',
            name='codigo',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]