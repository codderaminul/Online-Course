from django.db import models
from userPanel.models import User
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_phone = models.CharField(max_length=15,default=None,null=True, blank=True)
    user_location = models.CharField(max_length=100)
    user_image = models.CharField(max_length=200,default="/static/userPanel/files/PNG/login_image.png",null=True,blank=True)
    last_login = models.DateTimeField(default=None, null=True, blank=True)
    def __str__(self):
        return self.user.username

class ByCourse(models.Model):
    customer_id = models.IntegerField()
    course_id = models.IntegerField()


class OrderTable(models.Model):
    prod_id = models.CharField(max_length=50)
    prod_price = models.CharField(max_length=15)
    prod_quantity = models.CharField(max_length=15)
    mst_order_id = models.CharField(max_length=50)

class OrderMaster(models.Model):
    custmr_id = models.CharField(max_length=25,default=None)
    dele_chrg = models.CharField(max_length=25,default=None)
    shipper_name = models.CharField(max_length=50,default=None)
    billing_name = models.CharField(max_length=50,default=None)
    billing_adrs = models.CharField(max_length=50,default=None)
    payment_method = models.CharField(max_length=50,default=None)
    sub_total = models.CharField(max_length=25, default=None)
    price = models.CharField(max_length=25, default=None)





