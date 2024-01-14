from django.db import models

# from random import choice

# Create your models here.


# CHOICES = ("HEAD", "TAIL")


# class HeadTails(models.Model):
#     side = models.CharField(max_length=4, default=choice(CHOICES))
#     date = models.DateTimeField(auto_now_add=True)

#     def __str__(self) -> str:
#         return f"{self.date}: {self.side}"

#     @staticmethod
#     def get_static(times: int):
#         results = HeadTails.objects.order_by("date")[:times]
#         answer = {"HEAD": 0, "TAIL": 0}
#         for result in results:
#             answer[result.side] += 1
#         return str(answer)


# class Author(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField()
#     bio = models.TextField()
#     birthday = models.DateField(auto_now_add=True)
#     full_name = models.CharField(max_length=200)

#     def save(self, *args, **kwargs):
#         self.full_name = f"{self.first_name} {self.last_name}"
#         super(Author, self).save(*args, **kwargs)

#     def __str__(self) -> str:
#         return f"{self.first_name} {self.last_name}"


# class Article(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     pub_data = models.DateTimeField(auto_now_add=True)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     category = models.CharField(max_length=100)
#     view_count = models.IntegerField(default=0)
#     is_public = models.BooleanField(default=False)

#     def __str__(self) -> str:
#         return f"{self.title} by {self.author} {self.pub_data}"


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number_phone = models.CharField(max_length=16)
    address = models.TextField(max_length=100)
    date_registration = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Client: {self.name}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Product: {self.name}"


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Order list: {self.products} date: {self.date_ordered}"
