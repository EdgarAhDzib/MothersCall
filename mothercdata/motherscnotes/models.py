from django.db import models

# Create your models here.
class Characters(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=70,blank=True)
    notes = models.TextField(blank=True)
    relatives = models.TextField(blank=True)
    village = models.CharField(max_length=50,blank=True)
    elder = models.TextField(blank=True)
    def __str__(self):
        return self.name
class Diet(models.Model):
    name = models.CharField(max_length=50)
    indigenous = models.CharField(max_length=40,blank=True)
    def __str__(self):
        return self.name
class Supernatural(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=70,blank=True)
    notes = models.TextField(blank=True)
    def __str__(self):
        return self.name
class Flora(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=70,blank=True)
    notes = models.TextField(blank=True)
    indigenous = models.CharField(max_length=40,blank=True)
    classification = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.name
class Fauna(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=70,blank=True)
    notes = models.TextField(blank=True)
    indigenous = models.CharField(max_length=40,blank=True)
    classification = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.name
class Tech(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=70,blank=True)
    notes = models.TextField(blank=True)
    indigenous = models.CharField(max_length=40,blank=True)
    def __str__(self):
        return self.name
class Nature(models.Model):
    name = models.CharField(max_length=50)
    notes = models.TextField(blank=True)
    indigenous = models.CharField(max_length=40,blank=True)
    def __str__(self):
        return self.name
class Chapters(models.Model):
    name = models.CharField(max_length=50)
    notes = models.TextField(blank=True)
    chap_num = models.SmallIntegerField(null=True,blank=True)
    def __str__(self):
        return self.name
class Social(models.Model):
    name = models.CharField(max_length=50)
    notes = models.TextField(blank=True)
    def __str__(self):
        return self.name
