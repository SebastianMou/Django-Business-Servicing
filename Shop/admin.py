from django.contrib import admin
from .models import Category, Product, BottomFolder, Baner

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'old_price' , 'price', 'in_stock', 'created', 'updated']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'old_price', 'in_stock']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Baner)
class BanerAdmin(admin.ModelAdmin):
    list_display = ['titel_baner', 'img_baner']

@admin.register(BottomFolder)
class BottomFolderAdmin(admin.ModelAdmin):
    list_display = ['description_folder', 'product1', 'useful_links1','contact1' , 'facebook']
