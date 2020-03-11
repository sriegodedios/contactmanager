# Generated by Django 3.0.2 on 2020-03-11 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_auto_20200311_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registereduser',
            name='Email',
            field=models.EmailField(error_messages={'unique': 'This email already exsists.'}, max_length=100, unique=True),
        ),
    ]