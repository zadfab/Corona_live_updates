from django.db import models

# Create your models here.
class dataabase(models.Model):
    user_id = models.AutoField
    user_name = models.CharField(max_length=10,default="unknown")
    session_time = models.CharField(max_length=20,default="")

    def __str__(self):
        return self.user_name