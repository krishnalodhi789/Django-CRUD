# Generated by Django 4.2.7 on 2023-12-05 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.CharField(max_length=100, null=True),
        ),
    ]