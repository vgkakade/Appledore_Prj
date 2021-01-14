from django.urls import path,include
from rest_auth.views import LoginView
from .views import ProfileView,AddressView,login,MyToken
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [
    path('register/',include('rest_auth.registration.urls')),
    # path('auth/', login, name='rest-login'),
    path('auth/', MyToken.as_view()),
    path('profile/', ProfileView.as_view(), name='usr-profile'),
    path('addr/', AddressView.as_view(), name='usr-address'),
    path('addr/<int:pk>', AddressView.as_view(), name='usr-address'),
]