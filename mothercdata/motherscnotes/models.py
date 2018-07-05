from django.db import models

# Create your models here.
class Characters(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=70)
    notes = models.TextField()
    relatives = models.TextField()
    village = models.CharField(max_length=50)
    elder = models.TextField()
    def __str__(self):
        return self.name
class Diet(models.Model):
    name = models.CharField(max_length=50)
    indigenous = models.CharField(max_length=40)
    def __str__(self):
        return self.name
class Supernatural(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=70)
    notes = models.TextField()
    def __str__(self):
        return self.name
class Flora(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=70)
    notes = models.TextField()
    indigenous = models.CharField(max_length=40)
    classification = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Fauna(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=70)
    notes = models.TextField()
    indigenous = models.CharField(max_length=40)
    classification = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Tech(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=70)
    notes = models.TextField()
    indigenous = models.CharField(max_length=40)
    def __str__(self):
        return self.name
class Nature(models.Model):
    name = models.CharField(max_length=50)
    notes = models.TextField()
    indigenous = models.CharField(max_length=40)
    def __str__(self):
        return self.name
class Chapters(models.Model):
    name = models.CharField(max_length=50)
    notes = models.TextField()
    chap_num = models.SmallIntegerField()
    def __str__(self):
        return self.name
class Social(models.Model):
    name = models.CharField(max_length=50)
    notes = models.TextField()
    def __str__(self):
        return self.name
