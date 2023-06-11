from django.db import models

class Medication(models.Model):
    name_of_medication = models.CharField(default="", max_length=64, blank=False, unique=False)
    capacity = models.PositiveSmallIntegerField(default=1, blank=False)
    start_date = models.DateField(blank=True, null=True)
    picture = models.ImageField(upload_to="pictures", blank=True, null=True)

    def name_and_capacity(self):
        return "{}, capacity: {}".format(self.name_of_medication, self.capacity)

    def __str__(self):
        return self.name_and_capacity()

