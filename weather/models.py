from django.db import models


class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class UserQuery(models.Model):
    user_ip = models.CharField(max_length=16)
    city_name = models.CharField(max_length=25)
    count = models.IntegerField()

    def __str__(self) -> str:
        return self.city_name
    
    
    