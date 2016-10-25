from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField(verbose_name='e-mail')

    def __str__(self):
        return ''.join([self.first_name, self.last_name])
