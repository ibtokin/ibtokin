from django.db import models
from datetime import date

#from django.template.defaultfilters import slugify


'''
Note: these models are not supposed to make sense.
In the event that you do find meaning in them, please
consult your doctor.
'''

class They(models.Model):
    name = models.CharField(max_length=100, blank=False)
    profile_url = models.URLField()
    def __str__(self):
        return self.name


class Content(models.Model):
    author = models.ForeignKey(They, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Originally Generated on ')
    content_url = models.URLField()
    image_url = models.URLField()
    count = models.IntegerField(default=0)
    def __str__(self):
        return self.title
