from django.db import models

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    guest_count = models.PositiveIntegerField()
    reservation_time = models.DateTimeField(auto_now=True)
    phone_number = models.CharField(max_length=15)
    comments = models.TextField(blank=True, null=True)
