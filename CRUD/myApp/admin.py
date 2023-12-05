from django.contrib import admin
from .models import myRecords,userPics,images,profile
# Register your models here.
admin.site.register(myRecords)
admin.site.register(userPics)
admin.site.register(images)
admin.site.register(profile)