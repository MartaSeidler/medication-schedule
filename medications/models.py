from django.db import models


UNITS = {
    ('ml', 'ml'),
    ('mg', 'mg'),
    ('pills', 'pills'),
    ('dose', 'dose')
}


class Medication(models.Model):
    name_of_medication = models.CharField(default="", max_length=64, blank=False, unique=False)
    times_per_day = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    dosage = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    unit = models.CharField(choices=UNITS, max_length=10, default='ml')

    picture = models.ImageField(upload_to="pictures", blank=True, null=True)

    def name_and_capacity(self):
        return "{}".format(self.name_of_medication)

    def __str__(self):
        return self.name_and_capacity()
