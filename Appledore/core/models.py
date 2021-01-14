from django.db import models

# Create your models here.
class Company(models.Model):
    company_code = models.PositiveIntegerField()
    company_name = models.CharField(max_length=150)

    class Meta:
        verbose_name ="Company"
        verbose_name_plural ="Companies"

    def __str__(self):
        return self.company_name


class Category(models.Model):
    category_name = models.CharField(max_length=150)

    class Meta:
        verbose_name ="Category"
        verbose_name_plural ="Categories"

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=150,blank=False)
    product_price = models.IntegerField(blank=False)
    product_quantity = models.DecimalField(max_digits=10, decimal_places=0)
    product_desc = models.CharField(max_length=255)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    prod_company = models.ForeignKey(Company, on_delete=models.SET_NULL,null=True)
    
    class Meta:
        verbose_name ="Product"
        verbose_name_plural ="Products"

    def __str__(self):
        return self.product_name


class ProductImage(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    thumb = models.ImageField(default='products/default.png', upload_to='products', max_length=100,blank=False,null=False)
    top_view = models.ImageField(upload_to='products', max_length=100,blank=True,null=True)
    front_view = models.ImageField(upload_to='products', max_length=100,blank=True,null=True)
    left_view = models.ImageField(upload_to='products', max_length=100,blank=True,null=True)
    right_view = models.ImageField(upload_to='products', max_length=100,blank=True,null=True)
    

    class Meta:
        verbose_name = "ProductImages"
        verbose_name_plural = "ProductImages"

    def __str__(self):
        return str(self.product_id)
