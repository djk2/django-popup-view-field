from django.db import models


class Country(models.Model):
    code = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=256)


class AP(models.Model):
    name=models.CharField(max_length=200)
    APid=models.CharField(max_length=200)
    description1= models.CharField(max_length=200)
    description2= models.CharField(max_length=200)
    description3= models.CharField(max_length=200)


RATING_CHOICES = (
    (1, 1),
    (2, 2)
)

class APReview(models.Model):
    atPat=models.ForeignKey(AP, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    selectionReason=models.CharField(max_length=200)
