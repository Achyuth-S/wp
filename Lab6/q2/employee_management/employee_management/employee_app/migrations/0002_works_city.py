# Generated by Django 5.2 on 2025-04-23 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='works',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
    ]
