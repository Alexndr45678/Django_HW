from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from hw2_app.models import Client

class Command(BaseCommand):
    help = "Delete client"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("--pk", type=int, required=True, help="ID client")

    def handle(self, *args: Any, **options: Any) -> str | None:
        client = Client.objects.filter(pk=options["pk"]).first()
        if client:
            client.delete()
            self.stdout.write(f"{client.name} deleted!")
        else:
            self.stdout.write(f"Client not found!")