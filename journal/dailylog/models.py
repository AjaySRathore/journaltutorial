from django.db import models

# Create your models here.
class Day(models.Model):
    day = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.day)

class Gratitude(models.Model):
    gratitude = models.CharField(max_length=1000)
    day_id = models.ForeignKey(Day,on_delete=models.PROTECT)
