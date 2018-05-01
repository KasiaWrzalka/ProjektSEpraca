from django.core.management.base import BaseCommand, CommandError
from django.db import connection, OperationalError

class Command(BaseCommand):
    help = 'Uzupełnia tabele Conditions'

    def handle(self, *args, **options):
        print("start")
        cursor = connection.cursor()
        factors = "SELECT id, letter FROM `home_factors`"
        print(factors)
        # results = "SELECT id, title FROM `home_results`"
        cursor.execute(factors)
        z = cursor.fetchall()
        print(z)
        # cursor.execute(sql)
        cursor.close()

        print("end")