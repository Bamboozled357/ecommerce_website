from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('shop/category', views.CategoryViewSet, basename='shop')

urlpatterns = [
    path('', include(router.urls)),
    path('shop/category/<int:category_id>/item/', views.ItemListCreateAPIView.as_view()),
    path('shop/category/<int:category_id>/item/<int:pk>/', views.ItemRetrieveUpdateDestroyAPIView.as_view()),
    path('shop/category/<int:category_id>/item/<int:item_id>/order/', views.OrderListCreateAPIView.as_view()),
    path('shop/category/<int:category_id>/item/<int:item_id>/order/<int:pk>/', views.OrderRetrieveUpdateDestroyAPIView.as_view()),
]
