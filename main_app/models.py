from datetime import date
from django.db import models
from django.urls import reverse

VIEWS = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('N', 'Night'),
)


# Create your models here.

class House(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def get_absolute_url(self):
    return reverse('house_detail', kwargs={'house_id': self.id})

class Finch(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    class Meta: 
        verbose_name = 'finch'
        verbose_name_plural = 'finches'

    def __str__(self):
        return f'{self.name}, ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})

    def viewed_for_today(self):
        return self.watching_set.filter(date=date.today()).count() >= len(VIEWS)

class Watching(models.Model):
    date = models.DateField('viewing date')
    view = models.CharField(
        max_length=1,
        choices=VIEWS,
        default=VIEWS[0][0],
    )

    #create a finch_id FK
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_view_display()} on {self.date}"

    class Meta:
        ordering = ['-date']