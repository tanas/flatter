from django.core.management.base import BaseCommand
from tasks.utils import fetch_json
from tasks.models import Flat


class Command(BaseCommand):
    help = 'Parse..'
    url = 'https://ak.api.onliner.by/search/apartments'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        flats = fetch_json(self.url)

        for flat in flats['apartments']:
            id = flat['id']
            try:
                obj = Flat.objects.get(pk=id)
                print 'found'
            except Flat.DoesNotExist:
                obj = Flat(id=id,
                           data={})
                obj.save()
                print 'new flat'

