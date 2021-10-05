# Generated by Django 3.2.2 on 2021-06-08 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IEEE', '0002_auto_20210608_0758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='file',
        ),
        migrations.AddField(
            model_name='device',
            name='batteryStatus',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='changedTime',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='currentPowerSource',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='estimatedChargeRemaining',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]