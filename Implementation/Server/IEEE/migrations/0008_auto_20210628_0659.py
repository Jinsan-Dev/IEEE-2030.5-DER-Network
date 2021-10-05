# Generated by Django 3.2.2 on 2021-06-28 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IEEE', '0007_device_command'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='changedTime',
        ),
        migrations.AddField(
            model_name='device',
            name='passedTime',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='device',
            name='sfdi',
            field=models.CharField(default=0, max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='device',
            name='batteryStatus',
            field=models.IntegerField(default=1),
        ),
    ]