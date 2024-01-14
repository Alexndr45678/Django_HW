from typing import Any
from django.core.management.base import BaseCommand, CommandError, CommandParser
from hw2_app.models import Client, Product, Order


class Command(BaseCommand):
    help = "Creates new order"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("client_id", type=int, help="Client ID")
        parser.add_argument("product_id", type=int, help="Product ID")
        parser.add_argument("total_amount", type=float, help="Total Amount")

    def handle(self, *args, **kwargs):
        client_id, product_id, total_amount = (
            kwargs["client_id"],
            kwargs["product_id"],
            kwargs["total_amount"],
        )
        client = Client.objects.filter(pk=client_id).first()
        if not client:
            self.stdout.write(f"bad client id: {client_id}")
            return

        product = Product.objects.filter(pk=product_id).first()
        if not product:
            self.stdout.write(f"bad product id: {product_id}")
            return

        order = Order(client=client, total_amount=total_amount)
        order.save()
        order.products.add(product)
        self.stdout.write(f"{order}")
