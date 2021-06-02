from django.db import models

# Create your models here.
class Cart(models.Model):

    class Meta:
        db_table = 'Cart'

    def __str__(self):
        return 'Cart {}'.format(self.id)