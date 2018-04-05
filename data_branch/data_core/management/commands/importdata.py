from django.core.management.base import BaseCommand, CommandError
import csv
from data_core.models import *

class Command(BaseCommand):
    help = 'Import data from MySQL/csv to postgres corresponding model. Provide two arguments - File.csv and Model' \
           'The program can be run with the following command "python manage.py importdata <FileName.csv> <ClassName>".' \
           'It is going to get the data from the .csv file and import it in to the empty model. The .csv file sould ' \
           'be of type single column series i.e. "date" and "value" only! Aditional commands can be made for diffrent' \
           'type of data - multiple columns ect.'

    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str)
        parser.add_argument('class_name', type=str)

    def handle(self, *args, **options):
        try:
            with open('data_branch/data_core/old_data_temp/' + options['file_name']) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    p = eval(options['class_name'])(period=row['Period'], value=row['Value'])
                    p.save()
                csvfile.close()
                self.stdout.write(self.style.SUCCESS('Successfully added data to the database!'))
        except:
            raise CommandError('Something bad just happened! This error is comming from "data_core" app '
                               'custom management command "importdata"')
