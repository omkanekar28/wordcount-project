# Generated by Django 2.2.28 on 2023-09-01 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20230901_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='summary',
            field=models.CharField(default='', max_length=200),
        ),
    ]
