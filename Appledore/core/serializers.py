from rest_framework import serializers
from .models import Product,ProductImage,Company,Category

class ProductSerializer(serializers.ModelSerializer):
    # to pass all the images of a single project in one object
    thumb = serializers.SerializerMethodField()

    def get_thumb(self, obj):
        # get all objects
        request = self.context.get('request')
        x = ProductImage.objects.get(id=obj.id)
        return  request.build_absolute_uri(str(x.thumb.url))

    class Meta:
        model = Product
        fields = ['id','product_name','product_price','thumb','product_quantity']


class ProductDetailSerializer(serializers.ModelSerializer):
    thumb = serializers.SerializerMethodField(read_only=True)
    company = serializers.SerializerMethodField(read_only=True)
    category = serializers.SerializerMethodField(read_only=True)

    def get_thumb(self, obj):
        # current object's id is passed in ORM query
        obj = ProductImage.objects.get(id=obj.id)

        request = self.context.get('request')

        # used to return the domain path to the files
        image ={}

        image['thumb'] = request.build_absolute_uri(str(obj.thumb.url))
        if obj.top_view:
            image['top_view'] = request.build_absolute_uri(str(obj.top_view.url))
        if obj.front_view:
            image['front_view'] = request.build_absolute_uri(str(obj.front_view.url))
        if obj.left_view :
            image['left_view'] = request.build_absolute_uri(str(obj.left_view.url))
        if obj.right_view:
            image['right_view'] = request.build_absolute_uri(str(obj.right_view.url))
        return image

    def get_company(self, obj):
        obj = Product.objects.get(id=obj.id)
        company = Company.objects.get(id=obj.prod_company.id)
        if company:
            return str(company.company_name)

    def get_category(self,obj):
        obj = Product.objects.get(id=obj.id)
        category = Category.objects.get(id=obj.product_category.id)
        return str(category.category_name)


    class Meta:
        model = Product
        fields = ['id','product_name','product_price','product_quantity','product_desc','category','company','thumb']