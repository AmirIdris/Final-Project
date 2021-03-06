# Generated by Django 3.2 on 2021-05-04 20:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TrafficReport', '0005_alter_report_records'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True, verbose_name='Active')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='system_admin', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'SystemAdmin',
                'verbose_name_plural': 'SystemAdmins',
            },
        ),
    ]
