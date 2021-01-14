from django.contrib import admin
from .models import Category,Company,Product,ProductImage

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','category_name']

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id','company_name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','product_name','product_quantity']   

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product_id']