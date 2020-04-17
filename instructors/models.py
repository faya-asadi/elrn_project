from django.db import models

class Instructor(models.Model):
    name = models.CharField(max_length = 300)
    photo = models.ImageField(upload_to="photos/instructors")
    description = models.TextField(blank=True)
    email= models.CharField(max_length = 100)
    is_mvp = models.BooleanField(default=False)
    def __str__(self):
        return self.name
