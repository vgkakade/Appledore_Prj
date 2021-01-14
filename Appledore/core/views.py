from rest_framework import generics
from rest_framework.views import APIView
# from rest_framework.filters import SearchFilter,OrderingFilter
from .myPagination import MyPageNumberPagination
from django.http import JsonResponse
from .models import Product,Category,Company,ProductImage
from .serializers import ProductSerializer,ProductDetailSerializer

# Create your views here.
class ProductApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # implementing searching in existing api, no need to generate new one append search param in api
    # filter_backends = [SearchFilter,OrderingFilter]

    # ^ to indicate starts with, url ={{host}}/q=''
    # search_fields = ['product_name']

    # if - is used wile passing paramter descending order will be used
    # ordering_fields = ['product_name','product_price']
    # ordering_fields = '__all__'

    # pagination_class = MyPageNumberPagination
    

class ProductDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        product = Product.objects.get(id=pk)
        serializer = ProductDetailSerializer(product,context={"request": request})
        return JsonResponse(serializer.data)
