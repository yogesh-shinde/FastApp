from django.db import models
from User.models import User

# Create your models here.


class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=36)
    service_type = models.CharField(max_length=36)
    service_product = models.CharField(max_length=36)
    service_description = models.CharField(max_length=36)
    service_verify = models.BooleanField(default=False)
    service_email = models.EmailField(null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (f'{self.service_name}')
