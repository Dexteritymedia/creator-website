from django.db import models
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Activity Categories'

    def __str__(self):
        return self.name.title()
    
class Activity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100, blank=True)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    energy_level = models.IntegerField(
        help_text="0 for very relaxing, 100 for very energetic",
        null=True, blank=True,
    )
    stress_level = models.IntegerField(
        help_text="0 for very relaxing, 100 for high intensity",
        null=True, blank=True,
    )
    pic = models.ImageField(upload_to='pictures/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='activities')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Activities'

    
class Reservation(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.activity.name

class Budget(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.amount


class SavedBudget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    activities = models.ManyToManyField(Activity)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.amount

    
