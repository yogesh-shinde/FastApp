from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=36)
    user_username = models.CharField(max_length=36)
    user_password = models.CharField(max_length=36)
    user_confirm_password = models.CharField(max_length=36)
    user_email = models.EmailField()
    user_contact = models.IntegerField()

    def __str__(self):
        return self.user_name
