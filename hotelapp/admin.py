from django.contrib import admin
from.models import Customer, ImageRoom, Room,Discount,BookRoom,ExtraService,ServiceRoom
# Register your models here.
admin.site.register(Room)
admin.site.register(Customer)
admin.site.register(ImageRoom)
admin.site.register(Discount)
admin.site.register(BookRoom)
admin.site.register(ExtraService)
admin.site.register(ServiceRoom)