from django.db import models
from users.models import User
from django.utils.html import escape
# Create your models here.

class CatgoryProduct(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    foreign_key = models.ForeignKey(to=CatgoryProduct, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='images/products/product_pictures', null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    update_date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Basket(models.Model):
    user_for_basket = models.ForeignKey(to=User, related_name='user_for_basket', on_delete=models.CASCADE)
    product_for_basket = models.ForeignKey(to=Product, related_name='product_for_basket', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def update_total_price(self):
        return self.product_for_basket.price * self.quantity
    
    def increase_quantity(self):
        self.quantity += 1
        self.save()

    def decrease_quantity(self):
        if self.quantity > 1:
            self.quantity -= 1
            self.save()
        else:
            self.delete()

    def __str__(self):
        return f"{self.user_for_basket}"
    

class DeliveriInformation(models.Model):
    basket = models.ForeignKey(to=Basket, related_name='basket', on_delete=models.CASCADE)
    basket_information = models.TextField(default="Ничего нет")
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=200)
    numder_of_house = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    date_added = models.DateTimeField(auto_now_add=True)
    CHOOSE_METHOD = (('П', 'Оплата при получении'), ('К', 'Оплата на карту'))
    choose_payment_method = models.CharField(max_length=1, choices=CHOOSE_METHOD, default="Ничего не выбрано")

    class Meta:
        verbose_name = "Информация о доставке"
        verbose_name_plural = "Информация о доставках"

    def __str__(self):
        return f"{self.basket.user_for_basket.number_of_phone}"
    

class Comments(models.Model):
    user = models.ForeignKey(to=User, related_name='user', on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, related_name='product', on_delete=models.CASCADE)
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Пользователь - {self.user} оставил комментарий: {self.comment}"

