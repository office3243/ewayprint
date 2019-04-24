from django.db import models
from django.db.models.signals import post_save, pre_save
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import random
from django.core.validators import FileExtensionValidator


def create_customer(sender, created, instance, *args, **kwargs):
    if created:
        Customer.objects.create(user=instance, name=instance.username, email=instance.email)
    else:
        customer = instance.customer
        if customer.email != instance.email:
            customer.name = instance.username
            customer.email = instance.email
            customer.save()


post_save.connect(create_customer, sender=User)


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    phone = models.CharField(max_length=13, blank=True)
    email = models.EmailField(max_length=32, blank=True)
    balance = models.FloatField(default=500.0)

    def __str__(self):
        return self.name


PAYMENT_CHOICES = [('AC', 'Account'), ('CO', 'Coin')]
COLOR_MODEL_CHOICES = [('BW', 'Black&White'), ('CL', 'Colorful')]


ALLOWED_EXTENSIONS = ('jpg', 'png', 'pdf', 'jpeg', 'doc', 'docx', 'txt', 'odt',
                      'odp', 'ods', 'xls', 'xlsx', 'ppt', 'pptx', 'rtf')


class Transaction(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    upload_on = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='transaction_files/',
                            validators=[FileExtensionValidator(allowed_extensions=ALLOWED_EXTENSIONS), ])
    amount = models.FloatField(default=5.0)
    payment_mode = models.CharField(max_length=3, choices=PAYMENT_CHOICES)
    color_model = models.CharField(max_length=3, choices=COLOR_MODEL_CHOICES)
    otp_1 = models.IntegerField(blank=True, null=True)
    otp_2 = models.IntegerField(blank=True, null=True)
    printed = models.BooleanField(default=False)
    printed_datetime = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.customer.name

    class Meta:
        unique_together = ('otp_1', 'otp_2')


def save_otp(sender, instance, *args, **kwargs):
    while not (instance.otp_1 or instance.otp_2):
        try:
            instance.otp_1 = random.randint(1000, 9999)
            instance.otp_2 = random.randint(1000, 9999)
            instance.save()
        except:
            pass


post_save.connect(save_otp, sender=Transaction)
