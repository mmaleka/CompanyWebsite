from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    contact_name = models.CharField(max_length=50)
    contact_email = models.EmailField(max_length=100)
    content = models.CharField(max_length=500,)
    #user = models.ForeignKey(User)

    def __str__(self):
        return self.contact_name + ' - ' + self.content


class Signup(models.Model):
    contact_name = models.CharField(max_length=50)
    contact_email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return self.contact_name + ' - ' + self.contact_email
