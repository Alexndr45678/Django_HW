from typing import Any
from django.core.management.base import BaseCommand
from hw2_app.models import Article

class Command(BaseCommand):
    help = "Get all articles"

    def handle(self, *args: Any, **options: Any) -> str | None:
        articles = Article.objects.all()
        self.stdout.write(f"{articles}")