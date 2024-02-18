from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

from .models import Item, Category, Order
from .serializers import ItemSerializer, CategorySerializer, OrderSerializer
from .permissions import IsAuthorPermission, IsSenderPermission, IsBuyerPermission
from .pagination import StandardPagination


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    authentication_classes = [SessionAuthentication, TokenAuthentication, ]
    permission_classes = [IsSenderPermission,]
    pagination_class = StandardPagination


class ItemListCreateAPIView(ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication, ]
    permission_classes = [IsSenderPermission, ]

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return self.queryset.filter(category_id=category_id)

    def perform_create(self, serializer):
        category = self.kwargs.get('category_id')
        category = get_object_or_404(Category, id=category)
        serializer.save(profile=self.request.user, category=category)


class ItemRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication, ]
    permission_classes = [IsAuthorPermission, ]


class OrderListCreateAPIView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication, ]
    permission_classes = [IsBuyerPermission, ]

    def get_queryset(self):
        item_id = self.kwargs['item_id']
        return self.queryset.filter(item_id=item_id)

    def perform_create(self, serializer):
        item_id = self.kwargs['item_id']
        item = get_object_or_404(Item, id=item_id)
        serializer.save(profile=self.request.user, item=item)


class OrderRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication, ]
    permission_classes = [IsBuyerPermission, ]
