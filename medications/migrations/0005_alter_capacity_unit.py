# Generated by Django 4.2.2 on 2023-06-12 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0004_capacity_alter_medication_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capacity',
            name='unit',
            field=models.PositiveSmallIntegerField(choices=[(0, 'ml'), (1, 'mg'), (2, 'pills'), (3, 'dose')], default=0, max_length=10),
        ),
    ]
