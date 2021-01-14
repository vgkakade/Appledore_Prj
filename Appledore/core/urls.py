from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import ProductApiView,ProductDetailView

urlpatterns = [
    path('',ProductApiView.as_view(),name='core'),
    path('<int:pk>',ProductDetailView.as_view(),name='detail')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)