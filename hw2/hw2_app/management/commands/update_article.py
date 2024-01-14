from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from hw2_app.models import Article, Author


class Command(BaseCommand):
    help = "Update article"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("--title", type=str, help="new title")
        parser.add_argument("--date", type=str, help="new date")
        parser.add_argument("--pk", type=int, required=True, help="ID article")

    def handle(self, *args: Any, **options: Any) -> str | None:
        article = Article.objects.filter(pk=options["pk"]).first()
        if options.get("title"):
            article.title = options.get("title")
        if options.get("date"):
            article.title = options.get("date")
        article.save()
        self.stdout.write(f"{article}")