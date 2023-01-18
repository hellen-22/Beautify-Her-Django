from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from accounts.models import ServiceProvider, Customer

PAYMENT_STATUS_CHOICES = (
    ('Pending', 'Pending'),
    ('Complete', 'Complete'),
    ('Failed', 'Failed')
)


class ServiceCategory(models.Model):
    category_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category_name


class Service(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ServiceUpload(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE, related_name='provider')
    price = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(1)])
    images = models.ImageField(upload_to='images/services')
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return f'{self.service.name} , {self.provider.username}' 

class ProductCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='products/images')
    price = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(1)])
    slug = models.SlugField(null=True, blank=True)
    
    def __str__(self):
        return self.name

class Cart(models.Model):
    added_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.product.name

class Order(models.Model):
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=100, choices=PAYMENT_STATUS_CHOICES)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.customer.first_name

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name


class BookAppointment(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.service.name} 'on' {self.customer.first_name} 'by' {self.provider.user.first_name}"
