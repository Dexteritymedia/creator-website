from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
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
    date_submitted = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return self.name

class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question

class Stat(models.Model):
    subscribers = models.PositiveIntegerField(blank=True)
    views = models.PositiveIntegerField(blank=True)
    engagement = models.PositiveIntegerField(blank=True)

    def __str__(self):
        return f"Number of subscribers: {str(self.subscribers)}"
    
class Perk(models.Model):
    perk = models.CharField(max_length=100)

    def __str__(self):
        return self.perk

class WorkHistory(models.Model):
    RATINGS = (
        (5, '★★★★★'),
        (4, '★★★★'),
        (3, '★★★'),
        (2, '★★'),
        (1, '★'),
    )
    name = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    review = models.TextField()
    ratings = models.IntegerField(choices=RATINGS)
    client = models.CharField(max_length=100, blank=True)
    accept = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.review[:20]}..."
    
class CreatorDetail(models.Model):
    creator = models.CharField(max_length=50, null=True)
    tagline = models.TextField(blank=True)
    message = models.TextField()
    image = models.ImageField(upload_to='images', null=True, blank=True)
    video = models.FileField(upload_to='videos', null=True, blank=True)
    perks = models.ManyToManyField(Perk, default=None, blank=True, related_name="attributes")
    stats = models.ForeignKey(Stat, on_delete=models.CASCADE, null=True, blank=True)
    instagram_link = models.URLField(blank=True)
    facebook_link = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)
    tiktok_link = models.URLField(blank=True)
    youtube_link = models.URLField(blank=True)
    date_submitted = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"Last changes made was on {self.date_updated}"

    def save(self, *args, **kwargs):
        if CreatorDetail.objects.exists() and not self.pk:
            raise ValidationError("Only one instance of this page can be created.")
        super().save(*args, **kwargs)


class YouTubeVideo(models.Model):
    description = models.TextField(blank=True)
    youtube_link = models.URLField(blank=True)
    youtube_code = models.CharField(max_length=200, blank=True)

    def __str__(self):
        if self.description:
            return f"{self.description[:20]}..."
        elif self.youtube_link:
            return self.youtube_link
        else:
            return self.youtube_code

   
class Content(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    link = models.URLField(blank=True)
    youtube_video_link = models.ForeignKey(YouTubeVideo, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
