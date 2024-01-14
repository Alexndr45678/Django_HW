from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from hw2_app.models import Client


class Command(BaseCommand):
    help = "Add Client"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("name", type=str, help="Customer name")
        parser.add_argument("email", type=str, help="Customer email")
        parser.add_argument("number_phone", type=str, help="Customer number phone")
        parser.add_argument("address", type=str, help="Customer address")

    def handle(self, *args: Any, **kwargs: Any) -> str | None:
        name, email, number_phone, address = kwargs['name'], kwargs['email'], kwargs['number_phone'], kwargs['address']
        client = Client(name=name, email=email, number_phone=number_phone, address=address)
        client.save()
        self.stdout.write(f"{client.name} successfully added!")
