# Generated by Django 4.2 on 2023-04-28 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.IntegerField(primary_key='True', serialize=False),
        ),
    ]
