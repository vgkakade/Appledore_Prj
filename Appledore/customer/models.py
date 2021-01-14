from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator

# Create your models here.

ADDRESS_CHOICES = ( 
    ("Y", "Yes"), 
    ("N", "No")
) 

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_number = PhoneNumberField()

    class Meta:
        verbose_name ="Customer"
        verbose_name_plural ="Customers"

    def __str__(self):
        return self.user.first_name

class Address(models.Model):
    # although we are using object for mapping it internally uses id for performing operataions,
    # here id is serilization object id
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    house_no = models.CharField(max_length=50,blank=True)
    landmark = models.CharField(max_length=150,blank=True)
    area = models.CharField(max_length=150,blank=False)
    pincode = models.PositiveIntegerField(validators=[MaxValueValidator(999999)])
    city = models.CharField(max_length=150,blank=False)
    district = models.CharField(max_length=150,blank=False)
    state = models.CharField(max_length=150,blank=False)
    country = models.CharField(max_length=150,blank=False)
    alt_mobile_number = models.PositiveIntegerField(blank=True,null=True,validators=[MaxValueValidator(9999999999)])
    default_address = models.CharField(choices=ADDRESS_CHOICES,default='N',max_length=20)

    class Meta:
        verbose_name ="Address"
        verbose_name_plural ="Addresses"

    def __str__(self):
        return str(self.customer)


