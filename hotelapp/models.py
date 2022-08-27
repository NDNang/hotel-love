from django.db import models

# Create your models here.
class common(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    class Meta:
        abstract = True

class Customer(common):
    
    fullname= models.CharField(max_length=250)
    phone = models.IntegerField()
    sum_success = models.IntegerField(blank=True,null=True)
    sum_fail = models.IntegerField(blank=True,null=True)
    class Meta:
        db_table ="customer"
    

class Room(common):
    name= models.CharField(max_length=500)
    title= models.CharField(max_length=1000,blank=True,null=True)
    description = models.CharField(max_length=1000,blank=True,null=True)
    type = models.IntegerField(blank=True,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0,blank=True,null=True)
    images  = models.FileField(blank=True, null=True)
    class Meta:
        db_table="list_room"

class ImageRoom(common):
    title  = models.CharField(max_length=50)
    images  = models.FileField(blank=True, null=True)
    description  = models.CharField(max_length=1000,blank=True,null=True)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    class Meta:
        db_table ="image_room"

class ExtraService(common):
    name = models.CharField(max_length=500,blank=True,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0,blank=True,null=True)
    class Meta:
        db_table = "extra_service"

class BookRoom(common):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    date = models.DateTimeField()
    time_in = models.TimeField()
    time_out = models.TimeField()
    class Meta:
        db_table="book_room" 

class ServiceRoom(common):
    service = models.ForeignKey(ExtraService,on_delete=models.CASCADE)
    book_room = models.ForeignKey(BookRoom,on_delete=models.CASCADE)
    class Meta:
        db_table ="service_room"

class Discount(common):
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    percent = models.IntegerField(blank=True,null=True)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    class Meta:
        db_table ="discount_room"