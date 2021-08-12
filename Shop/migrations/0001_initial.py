# Generated by Django 3.2.6 on 2021-08-11 02:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(default='admin', max_length=255)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('in_stock', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('description_title', models.CharField(max_length=255, null=True)),
                ('title1', models.CharField(max_length=255, null=True)),
                ('img1', models.ImageField(null=True, upload_to='images/')),
                ('description1', models.TextField(blank=True)),
                ('title2', models.CharField(max_length=255, null=True)),
                ('img2', models.ImageField(null=True, upload_to='images/')),
                ('description2', models.TextField(blank=True)),
                ('title3', models.CharField(max_length=255, null=True)),
                ('img3', models.ImageField(null=True, upload_to='images/')),
                ('description3', models.TextField(blank=True)),
                ('title4', models.CharField(max_length=255, null=True)),
                ('img4', models.ImageField(null=True, upload_to='images/')),
                ('description4', models.TextField(blank=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='Shop.category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_creator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Products',
                'ordering': ('-created',),
            },
        ),
    ]
