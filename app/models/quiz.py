from django.db import models

from app.utils import blur_image


class QuizQuestion(models.Model):
    question_text = models.CharField(max_length=255)
    blurred_image = models.ImageField(upload_to='blurred_images/', null=True, blank=True)
    clear_image = models.ImageField(upload_to='clear_images/', null=True, blank=True)
    correct_option = models.CharField(max_length=255)
    option_one = models.CharField(max_length=255)
    option_two = models.CharField(max_length=255)
    option_three = models.CharField(max_length=255)
    has_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.clear_image and not self.blurred_image:
            blurred_image = blur_image(self.clear_image, blur_radius=25)
            self.blurred_image.save(self.clear_image.name, blurred_image, save=False)
            print(self.blurred_image, self.clear_image.path)

        super().save(*args, **kwargs)
        #super(QuizQuestion, self).save(*args, **kwargs)

    def __str__(self):
        return f"Question: {self.question_text[:50]}... Answer: {self.correct_option}"

        
    
