# Generated by Django 2.2 on 2019-04-24 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_auto_20190424_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='otp_1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='otp_2',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
