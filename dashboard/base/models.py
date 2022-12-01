from django.db import models

# make Accounts table
class Account(models.Model):
  summoner_name = models.CharField(max_length=50)
  summoner_level = models.IntegerField()
  summoner_rank = models.CharField(max_length=15, default='Unranked')

  def __str__(self):
    return self.summoner_level