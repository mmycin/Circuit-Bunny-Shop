from django.db import models
import uuid

class Item(models.Model):
    id = models.UUIDField(
        unique=True, 
        primary_key=True, 
        default=uuid.uuid4, 
        max_length=255, 
        editable=False
        )
    Title = models.CharField(max_length=40)
    Description = models.TextField()
    Previous_price = models.IntegerField()
    Current_price = models.IntegerField()
    Image_URL = models.URLField(default="")
    Category = models.CharField(default="", max_length=100)

    def __str__(self):
        return self.Title
    
class Announcement(models.Model):
    Image_URL = models.ImageField(upload_to="images")
    Title = models.CharField(max_length=40)
    Description = models.TextField()

    def __str__(self) :
        return self.Title
    
class CartItem(models.Model):
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.product.Title
    
class Preorder(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=250)
    Full_name = models.CharField(max_length=250)
    Address = models.CharField(max_length=250)
    Email = models.EmailField(max_length=254)
    Phone_number = models.CharField(max_length=15)

    def __str__(self):
        return str("Order no-" + str(self.id) + ": " + self.Name)

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    items = models.CharField(max_length=5000)
    Full_name = models.CharField(max_length=250)
    Address = models.CharField(max_length=250)
    Email = models.EmailField(max_length=254)
    Phone_number = models.CharField(max_length=15)
    TotalPrice = models.IntegerField(default=0)

    def __str__(self):
        return str("Order no-" + str(self.id))
    
class OrderUpdate(models.Model):
    id = models.AutoField(primary_key=True)
    Order_ID = models.IntegerField(default="")
    Description = models.CharField(max_length=5000)
    Timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return str("Tracker ID: " + str(self.Order_ID))
    
