from typing import Any
from django.core.management.base import BaseCommand
from hw2_app.models import Article, Author

class Command(BaseCommand):
    help = "Create new article"

    def handle(self, *args: Any, **options: Any) -> str | None:
        author = Author.objects.filter(pk=4).first()
        for i in range(1,6):
            article = Article(
                title=f"New article {i}",
                content=f"Some text of article {i}",
                author=author,
                category="Some category",
            )
            article.save()
            self.stdout.write(f"Article {i} added in table.")