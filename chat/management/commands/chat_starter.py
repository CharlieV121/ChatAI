from chat.main import Chat
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Initialize the Django project'

    def handle(self, *args, **options):
        Chat.get_instance()
        pass