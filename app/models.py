from django.db import models

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.email

class Details(models.Model):
    movie_name = models.CharField(max_length=50)
    movie_number = models.IntegerField()
    movie_year = models.DateField()
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='details')

