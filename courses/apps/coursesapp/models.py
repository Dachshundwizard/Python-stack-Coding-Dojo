from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model): # Class is a special keyword that indicates that we are defining an object.
# Now I will define my properties here. models.CharField, models.TextField, models.DateTimeField, models.ForeignKey
    course_name = models.CharField(max_length = 150)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True) # Will initialize with add, the time of creation
    updated_at = models.DateTimeField(auto_now = True)
