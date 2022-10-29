from django.db import models
  
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=256)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField()
    slug = models.SlugField(unique=True, null=False, blank=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='products')
    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(default=0)
    in_stock = models.BooleanField(default=True)
    quantity = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name