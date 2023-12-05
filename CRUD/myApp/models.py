from django.db import models

# Create your models here.
class myRecords(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobileNO=models.CharField(max_length=15)
    city= models.CharField(max_length=100)

class userPics(models.Model):
    user = models.ForeignKey(myRecords,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', null=True, blank=True)


class images(models.Model):
    image=models.ImageField(null=True, blank=True, upload_to='Images')


class profile(models.Model):
    name=models.CharField(max_length=100)
    mobile  = models.CharField(max_length=100,null=True)
    pic = models.ImageField(upload_to='images',null=True, blank=True,)

    def __str__(self) -> str:
        return self.name