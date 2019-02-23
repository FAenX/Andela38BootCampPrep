from django.db import models

# Create your models here.


class Andelan(models.Model):
    """[summary]

    Arguments:
        models {[type]} -- [description]
    """

    LANGUAGE_CHOICES = [
        ('Python', 'python'),
        ('Javascript', 'javascript'),
        ('Java', 'java'),
    ]
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    language = models.CharField(max_length=30, choices=LANGUAGE_CHOICES)

    def __str__(self):
        return f'{self.first_name} {self.second_name} is doing {self.language}'
