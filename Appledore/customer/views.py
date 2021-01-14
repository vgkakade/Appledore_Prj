from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated

# from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from django.contrib.auth import authenticate
from rest_framework import permissions
from django.contrib.auth.models import User
from .models import Address, Customer
from .serializer import UserSerializer, AddressSerializer,UserTokenObtainPairSerializer

# Create your views here.
@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'}, status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key,
                    'username':username}, status=HTTP_200_OK)


class MyToken(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserTokenObtainPairSerializer


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user_data = User.objects.get(id=self.request.user.id)

        serializer = UserSerializer(user_data)
        return JsonResponse(serializer.data)

    def post(self,request):
        ser = UserSerializer(data=request.data)
        obj = Customer.objects.get(user=request.user.id)
        obj.mobile_number = request.data['mobile_number']
        if ser.is_valid():
            obj.save()
            return JsonResponse({"Success":"Mobile Number updated"})
        else:
            return JsonResponse(ser.errors)

class AddressView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        address = Address.objects.filter(customer=self.request.user.id)
        serializer = AddressSerializer(address, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    def post(self, request, pk):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():  
            try:
                addr = Address.objects.get(id=pk)

                addr.house_no = request.data['house_no'],
                # addr.customer = request.user,
                addr.landmark = request.data['landmark'],
                addr.area = request.data['area'],
                pincode = request.data['pincode'],
                addr.pincode=(pincode)[0]
                addr.city = request.data['city'],
                addr.district = request.data['district'],
                addr.state = request.data['state'],
                addr.country = request.data['country'],
                
                addr.alt_mobile_number = request.data['alt_mobile_number'],
                addr.default_address = request.data['default_address']

                print(request.data['pincode'])

                addr.save()
            except Address.DoesNotExist:
                Address.objects.create(
                    customer = request.user,
                    house_no = request.data['house_no'],
                    landmark = request.data['landmark'],
                    area = request.data['area'],
                    pincode = request.data['pincode'],
                    city = request.data['city'],
                    district = request.data['district'],
                    state = request.data['state'],
                    country = request.data['country'],
                    alt_mobile_number = request.data['alt_mobile_number'],
                    default_address = request.data['default_address']
                )
            addr.save()
            return JsonResponse({"Success":"Saved"})
        else:
            return JsonResponse(serializer.errors)
    
    # def patch(self, request):
    #     serializer = AddressSerializer(data=request.data)
    #     addr = Address.objects.get(id=)

        
