
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('Shop:category_list', args=[self.slug])

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='product_creator', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    description_title = models.CharField(max_length=255, null=True)

    title1 = models.CharField(max_length=255, null=True)
    img1 = models.ImageField(upload_to='images/', null=True)
    description1 = models.TextField(blank=True)

    title2 = models.CharField(max_length=255, null=True)
    img2 = models.ImageField(upload_to='images/', null=True)
    description2 = models.TextField(blank=True)

    title3 = models.CharField(max_length=255, null=True)
    img3 = models.ImageField(upload_to='images/', null=True)
    description3 = models.TextField(blank=True)

    title4 = models.CharField(max_length=255, null=True)
    img4 = models.ImageField(upload_to='images/', null=True)
    description4 = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('Shop:product_detail', args=[self.slug])

    def __str__(self):
        return self.title

class BottomFolder(models.Model):
    description_folder = models.TextField(blank=True)

    product1 = models.CharField(max_length=255)
    product2 = models.CharField(max_length=255)
    product3 = models.CharField(max_length=255)
    product4 = models.CharField(max_length=255)

    useful_links1 = models.CharField(max_length=255)
    useful_links2 = models.CharField(max_length=255)
    useful_links3 = models.CharField(max_length=255)
    useful_links4 = models.CharField(max_length=255)

    contact1 = models.CharField(max_length=255)
    contact2 = models.CharField(max_length=255)
    contact3 = models.CharField(max_length=255)
    contact4 = models.CharField(max_length=255)

    instagrm = models.CharField(max_length=255)
    reddit = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    email = models.CharField(max_length=255)


    def __str__(self):
        return self.description_folder
