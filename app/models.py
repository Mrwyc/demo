from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.



class Fraction(models.Model):
    client = models.CharField(verbose_name='客户端', max_length=16)
    score = models.IntegerField(verbose_name='分数', default=0,
                                validators=[MaxValueValidator(10000000), MinValueValidator(1)])
