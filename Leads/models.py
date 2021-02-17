from django.db import models

# Create your models here.

class Lead(models.Model):

  SOURCE_CHOICES = (
    # the first value will be stored to the database and the second value is what will be displayed
    ('Youtube', 'Youtube'),
    ('Google', 'Google'),
    ('Newsletter', 'Newletter'),
  )

  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  age = models.IntegerField(default=0)

  phoned = models.BooleanField()
  source = models.CharField(choices=SOURCE_CHOICES, max_length=100)

  #  blank=True means that it can be an empty string
  #  null=True means that it can be NULL will be stored in the database
  profile_picture = models.ImageField(blank=True, null=True)
  special_files = models.FileField(blank=True, null=True)