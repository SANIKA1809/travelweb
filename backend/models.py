from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime    
# Create your models here.

class City(models.Model):
  name = models.CharField(max_length=32)
  description = models.CharField(max_length=1028)
  ratings = models.IntegerField(blank=True, null=True, default=1, validators = [MinValueValidator(0), MaxValueValidator(5)])
  hotels = models.IntegerField(blank=False, null=False, default=0, validators = [MinValueValidator(0), MaxValueValidator(2000)])
  gardens = models.IntegerField(blank=False, null=False, default=0, validators = [MinValueValidator(0), MaxValueValidator(200)])

  REQUIRED_FIELDS = ["name", "description"]

  class Meta:
    ordering = ["name"]
    unique_together = [["name"]]
    indexes = [
      models.Index(fields = ["name"], name ="city-db-name-idx")
    ]
    db_table = "m_city"


class Itinerary(models.Model):
  city = models.ForeignKey(City(), null = False, on_delete = models.CASCADE, related_name="itinerary_city")
  start_day = models.DateField()
  end_day =  models.DateField()
  peoples = models.IntegerField(blank = False, null = False, default = 0, validators = [MinValueValidator(1), MaxValueValidator(100)])

  REQUIRED_FIELDS = ["city", "start_day", "end_day", "peoples"]

  class Meta:
    ordering = ["id"]
    # unique_together = [["name"]]
    indexes = [
      models.Index(fields = ["start_day"], name ="itinerary-db-name-idx")
    ]
    db_table = "m_itinerary"


class Planning(models.Model):
  itinerary = models.ForeignKey(Itinerary(), null = False, on_delete = models.CASCADE, related_name="itinerary_city")
  day = models.DateField()
  activity = models.TextField()

  REQUIRED_FIELDS = ["itinerary", "day", "activity"]

  class Meta:
    ordering = ["day"]
    # unique_together = [["name"]]
    indexes = [
      models.Index(fields = ["day"], name ="planning-db-itinerary-idx")
    ]
    db_table = "m_planning"

class Review(models.Model):
    city1 = models.CharField(max_length=100)  # You can customize fields based on your requirements
    user_name = models.CharField(max_length=50)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.user_name}'s Review for {self.city}"