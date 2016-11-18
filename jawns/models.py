from django.db import models

'''
Note: these models are not supposed to make sense.
In the event that you do find meaning in them,
consult your doctor.
'''
class They(models.Model):
    title = models.Charfield(max_length=100)
    date = models.DateTimeField('Created')


class Content(models.Model):
    they = models.ForeignKey(They, on_delete=models.CASCADE)
    description = models.Charfield(max_length=200)
    url = models.URLField()
    image_url = models.URLField()
    count = models.IntegerField(default=0)
