from typing import Any
from django.core.management.base import BaseCommand
from hw2_app.models import Author

class Command(BaseCommand):
    help = "Create author"

    def handle(self, *args: Any, **options: Any) -> str | None:
        author = Author(first_name="Tom", last_name="Black")
        author.save()
        self.stdout.write(f"{author}: {author.first_name} {author.last_name}")