# Generated by Django 3.1.4 on 2020-12-25 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0002_auto_20201225_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
