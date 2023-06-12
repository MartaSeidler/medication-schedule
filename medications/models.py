from django.db import models


UNITS = {
    ('ml', 'ml'),
    ('mg', 'mg'),
    ('pills', 'pills'),
    ('dose', 'dose')
}


class Capacity(models.Model):
    unit = models.CharField(choices=UNITS, max_length=10)

    def __str__(self):
        return "{}".format(self.unit)


class Medication(models.Model):
    name_of_medication = models.CharField(default="", max_length=64, blank=False, unique=False)
    capacity = models.PositiveSmallIntegerField(default=1, blank=False)
    capacity_unit = models.OneToOneField(Capacity, on_delete=models.CASCADE, null=True, blank=True)
    start_date = models.DateField(blank=True, null=True)
    picture = models.ImageField(upload_to="pictures", blank=True, null=True)

    def name_and_capacity(self):
        return "{}, capacity: {}".format(self.name_of_medication, self.capacity)

    def __str__(self):
        return self.name_and_capacity()
