from django.db import models
from datetime import datetime
from instructors.models import Instructor
from categories.models import Category

class Course(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.DO_NOTHING)  
    category =  models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length = 200)
    description = models.TextField()
    level = models.IntegerChoices('level', 'beginner intermediate advanced') # enum
    photo = models.ImageField(upload_to="photos/courses")
    price = models.DecimalField(max_digits =6, decimal_places=2)
    is_published = models.BooleanField(default=True)
    created_date = models.DateTimeField(default = datetime.now)
    def __str__(self):
        return self.title
