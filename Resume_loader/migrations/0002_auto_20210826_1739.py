# Generated by Django 3.1.5 on 2021-08-26 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resume_loader', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=100),
        ),
    ]
