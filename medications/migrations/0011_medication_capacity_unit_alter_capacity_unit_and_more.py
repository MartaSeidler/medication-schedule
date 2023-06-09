# Generated by Django 4.2.2 on 2023-06-12 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0010_rename_capacity_capacity_amount_alter_capacity_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='medication',
            name='capacity_unit',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medications.capacity'),
        ),
        migrations.AlterField(
            model_name='capacity',
            name='unit',
            field=models.PositiveSmallIntegerField(choices=[(1, 'mg'), (3, 'dose'), (0, 'ml'), (2, 'pills')], default=0),
        ),
        migrations.AlterField(
            model_name='medication',
            name='capacity',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
