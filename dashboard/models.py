from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ReadLater(models.Model):
    url_name=models.URLField(max_length=300)
    title=models.CharField(max_length=300)
    name=models.ForeignKey(User,null=False,on_delete=models.CASCADE,db_column="username")
    
    def __str__(self):
        return f'{self.url_name}{self.title}'

class LikedNews(models.Model):
    url_name=models.URLField(max_length=300)
    title=models.CharField(max_length=300)
    name=models.ForeignKey(User,null=False,on_delete=models.CASCADE,db_column="username")
    
    def __str__(self):
        return f'{self.url_name}{self.title}'


class Catagory(models.Model):
    fav1=models.CharField(max_length=300,default="Nothig")
    fav2=models.CharField(max_length=300,default="Nothig")
    fav3=models.CharField(max_length=300,default="Nothig")
    fav4=models.CharField(max_length=300,default="Nothig")
    fav5=models.CharField(max_length=300,default="Nothig")
    name=models.ForeignKey(User,null=False,on_delete=models.CASCADE,db_column="username")
    
    def __str__(self):
        return f'{self.fav1}{self.fav2}{self.fav3}{self.fav4}{self.fav5}'



