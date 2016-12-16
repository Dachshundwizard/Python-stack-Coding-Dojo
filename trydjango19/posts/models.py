from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Post(models.Model): #this is a python class.
    title = models.CharField(max_length=120)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)# everytime it is saved, theis time is set.
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)# whenever this is initially saved, it is set once.

    def __unicode__(self): # This is needed for Python to be able to print readable representation when you call an object. Without it, it will say {post object}
        return self.title

    def get_absolut_url(self):
        return "/"
