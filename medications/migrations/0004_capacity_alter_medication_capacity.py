# Generated by Django 4.2.2 on 2023-06-12 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0003_medication_name_of_medication'),
    ]

    operations = [
        migrations.CreateModel(
            name='Capacity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.PositiveSmallIntegerField(max_length=10)),
                ('unit', models.PositiveSmallIntegerField(choices=[(0, 'ml'), (1, 'mg'), (3, 'dose'), (2, 'pills')], default=0, max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='medication',
            name='capacity',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='medications.capacity'),
        ),
    ]