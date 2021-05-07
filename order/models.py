from django.db import models

# Create your models here.
class Orders(models.Model):  
    customername = models.CharField(max_length=200)  
    customerphone = models.CharField(max_length=20)  
    customeremail = models.EmailField()  
    totalordersum=models.IntegerField()
    class Meta:  
        db_table = "orders"  