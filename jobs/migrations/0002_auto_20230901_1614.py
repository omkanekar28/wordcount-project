# Generated by Django 2.2.28 on 2023-09-01 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
