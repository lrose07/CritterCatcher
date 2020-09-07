from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class CritterType(models.Model):
    critter_type = models.CharField(max_length=20)

    def __str__(self):
        return self.critter_type


class Location(models.Model):
    location = models.CharField(max_length=20)
    type = models.ForeignKey(CritterType, on_delete=models.PROTECT)

    def __str__(self):
        return self.location


class Critter(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(CritterType, on_delete=models.PROTECT)
    location = models.ForeignKey(Location, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.name


class Hour(models.Model):
    hour = models.IntegerField(validators=[MaxValueValidator(23), MinValueValidator(0)])

    def __str__(self):
        return str(self.hour)


class CritterTimeRelationship(models.Model):
    critter = models.ForeignKey(Critter, on_delete=models.CASCADE)
    hour = models.ForeignKey(Hour, on_delete=models.PROTECT)

    def __str__(self):
        return self.critter


class Month(models.Model):
    month = models.IntegerField(validators=[MaxValueValidator(12), MinValueValidator(1)])

    def __str__(self):
        return str(self.month)


class Hemisphere(models.Model):
    hemisphere = models.CharField(max_length=20)

    def __str__(self):
        return self.hemisphere


class CritterMonthHemisphereRelationship(models.Model):
    critter = models.ForeignKey(Critter, on_delete=models.CASCADE)
    month = models.ForeignKey(Month, on_delete=models.PROTECT)
    hemisphere = models.ForeignKey(Hemisphere, on_delete=models.PROTECT)

    def __str__(self):
        return self.critter
