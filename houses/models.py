from django.db import models

# Create your models here.
class House(models.Model):

    AREA_UNIT_CHOICES = [
        ('SqFt', 'SqFt'),
    ]

    HOME_TYPE_CHOICES = [
        ('Apartment', 'Apartment'),
        ('Condominium', 'Condominium'),
        ('Condominium', 'Condominium'),
        ('Duplex', 'Duplex'),
        ('home_type', 'home_type'),
        ('Miscellaneous', 'Miscellaneous'),
        ('MultiFamily2To4', 'MultiFamily2To4'),
        ('SingleFamily', 'SingleFamily'),
        ('VacantResidentialLand', 'VacantResidentialLand'),
    ]

    area_unit = models.CharField(max_length=10, choices=AREA_UNIT_CHOICES, null=True)
    bathrooms = models.FloatField(blank=True, null=True)
    bedrooms = models.PositiveSmallIntegerField(null=True)
    home_size = models.PositiveSmallIntegerField(blank=True, null=True)
    home_type = models.CharField(max_length=50, choices=HOME_TYPE_CHOICES, null=True)
    last_sold_date = models.DateField(null=True, blank=True)
    last_sold_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    link = models.URLField(null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    property_size = models.PositiveSmallIntegerField(blank=True, null=True)
    rent_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    rentzestimate_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    rentzestimate_last_updated = models.DateField(null=True, blank=True)
    tax_value = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    tax_year = models.PositiveSmallIntegerField(null=True)
    year_built = models.PositiveSmallIntegerField(blank=True, null=True)
    zestimate_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    zestimate_last_updated = models.DateField(null=True, blank=True)
    zillow_id = models.PositiveIntegerField(null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=3, null=True)
    zipcode = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.home_size}{self.area_unit} {self.home_type} {self.year_built} year build, {self.bedrooms} bedrooms, {self.bathrooms} bathrooms in {self.city}({self.state}) {self.address} for ${self.price}'
