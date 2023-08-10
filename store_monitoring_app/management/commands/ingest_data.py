# store_monitoring_app/management/commands/ingest_data.py

import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from store_monitoring_app.models import StoreStatus, BusinessHours, StoreTimezone

class Command(BaseCommand):
    help = 'Ingest data from CSVs into the database'

    def handle(self, *args, **kwargs):
        # Load data from store status.csv into StoreStatus model
        with open('store status.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                StoreStatus.objects.create(
                    store_id=int(row['store_id']),
                    timestamp_utc=datetime.strptime(row['timestamp_utc'], '%Y-%m-%d %H:%M:%S'),
                    status=row['status']
                )

        # Load data from Menu hours.csv into BusinessHours model
        with open('Menu hours.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                BusinessHours.objects.create(
                    store_id=int(row['store_id']),
                    day_of_week=int(row['dayOfWeek']),
                    start_time_local=datetime.strptime(row['start_time_local'], '%H:%M').time(),
                    end_time_local=datetime.strptime(row['end_time_local'], '%H:%M').time(),
                )

        # Load data from bq-results-20230125-202210-1674678181880.csv into StoreTimezone model
        with open('bq-results-20230125-202210-1674678181880.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                StoreTimezone.objects.create(
                    store_id=int(row['store_id']),
                    timezone_str=row['timezone_str'],
                )
