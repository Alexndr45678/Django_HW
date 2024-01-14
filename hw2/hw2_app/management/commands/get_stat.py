from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from hw2_app.models import HeadTails


class Command(BaseCommand):
    help = "Get static"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("--times", type=int, default=3, help="Count rows")

    def handle(self, *args: Any, **options: Any) -> str | None:
        count = options.get("times")
        self.stdout.write(HeadTails.get_static(count))
