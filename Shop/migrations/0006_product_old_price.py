# Generated by Django 3.2.6 on 2022-01-19 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0005_auto_20220119_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='old_price',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True),
        ),
    ]
