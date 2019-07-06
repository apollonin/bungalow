# Generated by Django 2.2.3 on 2019-07-06 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_unit', models.CharField(choices=[('SqFt', 'SqFt')], max_length=10, null=True)),
                ('bathrooms', models.FloatField(blank=True, null=True)),
                ('bedrooms', models.PositiveSmallIntegerField(null=True)),
                ('home_size', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('home_type', models.CharField(choices=[('Apartment', 'Apartment'), ('Condominium', 'Condominium'), ('Condominium', 'Condominium'), ('Duplex', 'Duplex'), ('home_type', 'home_type'), ('Miscellaneous', 'Miscellaneous'), ('MultiFamily2To4', 'MultiFamily2To4'), ('SingleFamily', 'SingleFamily'), ('VacantResidentialLand', 'VacantResidentialLand')], max_length=50, null=True)),
                ('last_sold_date', models.DateField(blank=True, null=True)),
                ('last_sold_price', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('link', models.URLField(null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('property_size', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('rent_price', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('rentzestimate_amount', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('rentzestimate_last_updated', models.DateField(blank=True, null=True)),
                ('tax_value', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('tax_year', models.PositiveSmallIntegerField(null=True)),
                ('year_built', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('zestimate_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('zestimate_last_updated', models.DateField(blank=True, null=True)),
                ('zillow_id', models.PositiveIntegerField(null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('city', models.CharField(max_length=200, null=True)),
                ('state', models.CharField(max_length=3, null=True)),
                ('zipcode', models.PositiveIntegerField(null=True)),
            ],
        ),
    ]
