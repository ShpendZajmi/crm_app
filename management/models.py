from types import CoroutineType
from xml.etree.ElementTree import Comment
from django.conf import settings
from django.db import models
from django.db.models import F
from django.contrib.auth.models import User
from django.forms import EmailField


# Create your models here.
STATUS = (
    ('1', 'INITIAL'),
    ('2', 'IN_PROGRESS'),
    ('3', 'COMPLETED'),
    

)


DEPARTMENT = (
    ('PRESS', 'PRESS'),
    ('DESIGN', 'DESIGN'),
    

)

MATERIAL = (
    ('FOLJE', 'FOLJE'),
    ('ALUBOND', 'ALUBOND'),
    

)
MACHINE = (
    ('MIMAKI', 'MIMAKI'),
    ('XEROX', 'XEROX'),
    

)

class Clients(models.Model):

        CompanyName = models.CharField(max_length=100, null=True)
        ContactPerson = models.CharField(max_length=100, null=True)
        Phone = models.CharField(max_length=100, null=True)
        Email = models.EmailField(max_length=100,null=True)
        City = models.CharField(max_length=100, null=True)
        Unique_number = models.CharField(max_length=100, null=True)
        Fiscal_number = models.CharField(max_length=100, null=True)
        Business_number = models.CharField(max_length=100, null=True)
        Address = models.CharField(max_length=100, null=True)
        Dateadded = models.DateTimeField(auto_now_add=True)
        #BusinessType
        Owner = models.ForeignKey(User,models.CASCADE,null=True)
        class Meta:
            verbose_name_plural = 'Clients'

        def __str__(self):
           return f'{self.CompanyName}'

        

class Orders(models.Model):

        CompanyName = models.ForeignKey(Clients, on_delete=models.CASCADE)
        Deadline = models.DateField(null=True)
        Dateadded = models.DateTimeField(auto_now_add=True)
        User = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
        DEPARTMENT = models.CharField(max_length=100,choices=DEPARTMENT,null=True)
        Comment = models.CharField(max_length=200,null=True)
        TotalPrice = models.FloatField(null=True)
        Status = models.CharField(max_length=20,choices=STATUS, null=True)
        class Meta:
            verbose_name_plural = 'Orders'

        def __str__(self):
            return f'Order {self.pk}'
            
   
            

class OrderItems(models.Model):

        CompanyName = models.ForeignKey(Orders,on_delete=models.CASCADE, null=True)
        Material = models.CharField(max_length=100,choices=MATERIAL,null=True)
        Machine = models.CharField(max_length=100,choices=MACHINE,null=True)
        Dimension1 = models.FloatField(null=True)
        Dimension2 = models.FloatField(null=True)
        Quantity = models.FloatField(null=True)
        Quantity_m2 = F('Dimension1') * F('Dimension2') * F('Quantity') / 10000
        project = models.CharField(max_length=100,null=True)
        price = models.FloatField(null=True)
        Mount = models.BooleanField(null=True)
        Comment = models.CharField(max_length=200,null=True)
        
        class Meta():
         verbose_name_plural = 'OrderItems'


