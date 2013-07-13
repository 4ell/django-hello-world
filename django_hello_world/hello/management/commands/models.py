from django.core.management.base import BaseCommand
from django.db import models


class Command(BaseCommand):
    args = ''
    help = 'Prints all project models'

    def handle(self, *args, **options):
        result = []
        resulte = []
        for model in models.get_models():
            result += [
                '\033[94m', model._meta.object_name, '\033[0m'
                '\n Count: ', str(model.objects.count()), '\n'
            ]
            resulte += [
                model._meta.object_name,
                '\n Count: ', str(model.objects.count()), '\n'
            ]
        result = ''.join(result)
        resulte = ''.join(resulte)
        self.stdout.write(result)
        self.stderr.write('error: ' + resulte)
