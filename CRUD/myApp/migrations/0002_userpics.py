# Generated by Django 4.2.7 on 2023-12-04 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userPics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.myrecords')),
            ],
        ),
    ]
