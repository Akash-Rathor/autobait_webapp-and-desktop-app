# Generated by Django 3.2.4 on 2021-07-14 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linkedincredentials',
            name='username',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
