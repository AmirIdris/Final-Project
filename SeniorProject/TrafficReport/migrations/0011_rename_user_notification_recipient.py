# Generated by Django 3.2 on 2021-06-03 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TrafficReport', '0010_notification_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='user',
            new_name='recipient',
        ),
    ]