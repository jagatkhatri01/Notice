# Generated by Django 5.0.1 on 2024-01-13 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0002_noticeboard_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticeboard',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]