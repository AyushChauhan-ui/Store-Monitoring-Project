from django.db import models

class StoreStatus(models.Model):
    store_id = models.IntegerField()
    timestamp_utc = models.DateTimeField()
    status = models.CharField(max_length=10)

class BusinessHours(models.Model):
    store_id = models.IntegerField()
    day_of_week = models.IntegerField(choices=[(i, i) for i in range(7)])
    start_time_local = models.TimeField()
    end_time_local = models.TimeField()

class StoreTimezone(models.Model):
    store_id = models.IntegerField()
    timezone_str = models.CharField(max_length=50)


# Create your models here.
