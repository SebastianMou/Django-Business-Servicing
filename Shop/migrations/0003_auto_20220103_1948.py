# Generated by Django 3.2.6 on 2022-01-03 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0002_product_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description4',
        ),
        migrations.RemoveField(
            model_name='product',
            name='img4',
        ),
        migrations.RemoveField(
            model_name='product',
            name='title4',
        ),
    ]
