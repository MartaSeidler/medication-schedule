from django.db import models
from django.utils import timezone


UNITS = {
    ('ml', 'ml'),
    ('mg', 'mg'),
    ('pcs', 'pcs'),
    ('dose', 'dose')
}


class Medication(models.Model):
    name_of_medication = models.CharField(default="", max_length=64, blank=False, unique=False)
    # time_1 = models.TimeField(auto_now=False, default=timezone.now)
    # dosage_1 = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    # unit_1 = models.CharField(choices=UNITS, max_length=10, default='ml')
    # time_2 = models.TimeField(auto_now=False, default=timezone.now)
    # dosage_2 = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    # unit_2 = models.CharField(choices=UNITS, max_length=10, default='ml')
    # time_3 = models.TimeField(auto_now=False, default=timezone.now)
    # dosage_3 = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    # unit_3 = models.CharField(choices=UNITS, max_length=10, default='ml')
    picture = models.ImageField(upload_to="pictures", blank=True, null=True)
    slug = models.SlugField(max_length=250)

    def name_of_medications(self):
        return "{}".format(self.name_of_medication)

    def __str__(self):
        return self.name_of_medication


class Dose(models.Model):
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE, related_name='doses')
    time = models.TimeField(auto_now=False, default=timezone.now)
    dosage = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    unit = models.CharField(choices=UNITS, max_length=10, default='ml')
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('time',)

    def __str__(self):
        return 'Dawka {} {} o godz. {} dla leku {} została utworzona.'.format(self.dosage, self.unit, self.time, self.medication)