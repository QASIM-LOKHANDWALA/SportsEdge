from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    age = models.IntegerField()
    height_cm = models.FloatField()
    weight_kgs = models.FloatField()
    positions = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    overall_rating = models.IntegerField()
    potential = models.IntegerField()
    value_euro = models.BigIntegerField()
    wage_euro = models.BigIntegerField()
    preferred_foot = models.CharField(max_length=10, null=True, blank=True)
    international_reputation = models.IntegerField(null=True, blank=True)
    weak_foot = models.IntegerField()
    skill_moves = models.IntegerField()
    body_type = models.CharField(max_length=50, null=True, blank=True)
    release_clause_euro = models.BigIntegerField(null=True, blank=True)
    crossing = models.IntegerField(null=True, blank=True)
    finishing = models.IntegerField(null=True, blank=True)
    dribbling = models.IntegerField(null=True, blank=True)
    vision = models.IntegerField(null=True, blank=True)
    penalties = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.full_name
