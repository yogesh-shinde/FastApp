from django.db import models

# Create your models here.


class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=36)
    admin_username = models.CharField(max_length=36, unique=True)
    admin_password = models.CharField(max_length=36)
    admin_confirm_password = models.CharField(max_length=36)
    admin_email = models.EmailField()
    admin_contact = models.IntegerField(unique=True)

    def __str__(self):
        return self.admin_name
