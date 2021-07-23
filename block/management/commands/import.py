import requests
from datetime import datetime

from django.core.management.base import BaseCommand

from block.models import Block

URL = 'https://bcschain.info/api/blocks'


class Command(BaseCommand):
    def handle(self, *args, **options):
        response = requests.get(url=URL).json()
        for block in response:
            Block.objects.update_or_create(
                height=block['height'],
                defaults={
                    'hash': block['hash'],
                    'time': datetime.fromtimestamp(block['timestamp']),
                    'address': block['miner'],
                    'count_of_transactions': block["transactionCount"],
                }
            )
