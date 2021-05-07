from django.db import models

# Create your models here.
class Product(models.Model):
    productcode=models.CharField(max_length=30)
    productname=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    unitprice=models.IntegerField()
    currentstock=models.IntegerField()
    
    class Meta:
        db_table="product"
    
    

    
    
    
