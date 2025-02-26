from django.db import models

class CricketPlayer(models.Model):
    id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    fullname = models.CharField(max_length=200)
    image_path = models.URLField(max_length=300)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=[('m', 'Male'), ('f', 'Female')])
    batting_style = models.CharField(max_length=100, blank=True, null=True)
    bowling_style = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=100)
    updated_at = models.DateTimeField()
    continent_id = models.IntegerField()
    continent_name = models.CharField(max_length=100)
    country_id = models.IntegerField()
    country_name = models.CharField(max_length=100)
    country_image_path = models.URLField(max_length=300)

    def __str__(self):
        return self.fullname
