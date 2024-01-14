from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from hw2_app.models import Article


class Command(BaseCommand):
    help = "Update article"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("--pk", type=int, required=True, help="ID article")

    def handle(self, *args: Any, **options: Any) -> str | None:
        article = Article.objects.filter(pk=options["pk"]).first()
        if article:
            article.delete()
            self.stdout.write(f"{article} deleted")
        else:
            self.stdout.write(f"Article is not found")
