from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    # license_number is deleted from here

    def __str__(self):
        return self.user.username

class Bike(models.Model):
    # ... existing fields ...
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    availability = models.BooleanField(default=True)
    daily_rate = models.DecimalField(max_digits=6, decimal_places=2, default=50.00)
    image_url = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.bike.availability = False
            self.bike.save()
        super().save(*args, **kwargs)

class Review(models.Model):
    bike = models.ForeignKey(Bike, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)]) # 1 to 5 stars
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.bike.model}"