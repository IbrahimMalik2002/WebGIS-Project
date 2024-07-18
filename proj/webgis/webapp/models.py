from django.db import models
# Create your models here.


class user_info(models.Model):
    password = models.CharField(max_length=20)
    username = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        db_table = "user_info"
