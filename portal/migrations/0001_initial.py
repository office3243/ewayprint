# Generated by Django 2.2 on 2019-04-24 17:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.EmailField(blank=True, max_length=32)),
                ('balance', models.FloatField(default=500.0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_on', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(upload_to='transaction_files/')),
                ('amount', models.FloatField(default=5.0)),
                ('payment_mode', models.CharField(choices=[('AC', 'Account'), ('CO', 'Coin')], max_length=3)),
                ('color_model', models.CharField(choices=[('BW', 'Black&White'), ('CL', 'Colorful')], max_length=3)),
                ('otp_1', models.IntegerField()),
                ('otp_2', models.IntegerField()),
                ('printed', models.BooleanField(default=False)),
                ('printed_datetime', models.DateTimeField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Customer')),
            ],
            options={
                'unique_together': {('otp_1', 'otp_2')},
            },
        ),
    ]
