from django.core.management.base import BaseCommand
from django.utils import timezone
import csv
import datetime

from houses.models import House

class Command(BaseCommand):
    help = 'Parse and loads data from challenge_data.csv'

    def add_arguments(self, parser):
        parser.add_argument('filename', help='CSV file to read from')


    def handle(self, *args, **kwargs):
        filename = kwargs['filename']

        self.stdout.write(self.style.SUCCESS("Start working with {}".format(filename)))

        with open(filename) as f:
            for row in csv.DictReader(f):
                house = self.create_house(row)
                self.stdout.write(str(house))
                house.save()
                # break

        self.stdout.write(self.style.SUCCESS("Done"))

    def create_house(self, row):
        row = self.parse_formats(row)
        house = House(**row)
        # print(house.price);exit()
        return house

    def parse_formats(self, row):
        # print(row);exit()
        try:
            row['bathrooms'] = float(row['bathrooms']) if row['bathrooms'] else None
            row['bedrooms'] = int(row['bedrooms'])
            row['home_size'] = int(row['home_size']) if row['home_size'] else None
            row['last_sold_date'] = self._parse_date(row['last_sold_date'])
            row['last_sold_price'] = self._parse_price(row['last_sold_price'])
            row['price'] = self._parse_price(row['price'])
            row['property_size'] = int(row['property_size']) if row['property_size'] else None
            row['rent_price'] = self._parse_price(row['rent_price'])
            row['rentzestimate_amount'] = self._parse_price(row['rentzestimate_amount'])
            row['rentzestimate_last_updated'] = self._parse_date(row['rentzestimate_last_updated'])
            row['tax_value'] = float(row['tax_value'])
            row['tax_year'] = int(row['tax_year'])
            row['year_built'] = int(row['year_built']) if row['year_built'] else None
            row['zestimate_amount'] = self._parse_price(row['zestimate_amount'])
            row['zestimate_last_updated'] = self._parse_date(row['zestimate_last_updated'])
            row['zillow_id'] = int(row['zillow_id'])
            row['zipcode'] = int(row['zipcode'])

            return row
        except Exception as e:
            self.stdout.write(self.style.WARNING(row))
            raise
        
        

    def _parse_date(self, date):
        if not date: return None

        return datetime.datetime.strftime(datetime.datetime.strptime(date, '%M/%d/%Y'), '%Y-%m-%d')

    def _parse_price(self, price):
        if not price: return None

        abbrs_to_power = {
            'K': 1e3,
            'M': 1e6,
            'B': 1e9
        }

        # remove $
        if price[0] == '$':
            price = price[1:]

        # parse K, M, B to power of 10
        if price[-1] in abbrs_to_power:
            abbr = price[-1]
            price = float(price[:-1]) * abbrs_to_power[abbr]

        return price

