from django.db import models


class City(models.Model):
    name = models.CharField(unique=True, max_length=256, blank=False)


class Street(models.Model):
    name = models.CharField(db_index=True, max_length=256, blank=False)
    city_id = models.ForeignKey('City', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'city_id')


class Shop(models.Model):
    name = models.CharField(db_index=True, max_length=256, blank=False)
    city_name = models.CharField(db_index=True, max_length=256, blank=False,
                                 default='')
    street_name = models.CharField(db_index=True, max_length=256, blank=False,
                                   default='')
    building = models.CharField(max_length=64, blank=False)
    work_from = models.TimeField(blank=True)
    work_to = models.TimeField(blank=True)
