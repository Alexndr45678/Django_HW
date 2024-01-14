from typing import Any
from django.core.management.base import BaseCommand
from hw2_app.models import HeadTails


class Command(BaseCommand):
    help = "Flip generate"

    def handle(self, *args, **options) -> str | None:
        money = HeadTails()
        money.save()
        self.stdout.write(str(money))
        
