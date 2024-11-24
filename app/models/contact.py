from django.core.validators import RegexValidator
from django.db import models

class Contact(models.Model):
    CHOICE = (
        ('Hire', 'I want to hire you'),
        ('Help', 'I need your help'),
    )
    
    email = models.EmailField()
    name = models.CharField(max_length=100)
    phone_no = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ],
        null=True, blank=True,
    )
    message = models.TextField(blank=True, null=True)
    choice = models.TextField(blank=True, null=True, choices=CHOICE)
    created_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.eamil} Created at: {self.created_at}"


class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return f"Question: {self.question[:50]}... Answer: {self.answer[:50]}..."
