from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class linkedincredentials(TimeStampMixin):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    username = models.CharField(max_length=200,unique=True)
    password = models.BinaryField(max_length=200)

