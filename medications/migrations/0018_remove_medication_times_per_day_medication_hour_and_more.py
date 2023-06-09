# Generated by Django 4.2.2 on 2023-06-15 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0017_remove_medication_capacity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medication',
            name='times_per_day',
        ),
        migrations.AddField(
            model_name='medication',
            name='hour',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medication',
            name='unit',
            field=models.CharField(choices=[('ml', 'ml'), ('dose', 'dose'), ('mg', 'mg'), ('pills', 'pills')], default='ml', max_length=10),
        ),
    ]
