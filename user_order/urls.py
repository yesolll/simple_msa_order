from django.urls import path
from .views import ShopViewSet, OrderViewSet

urlpatterns = [
    path('shop', ShopViewSet.as_view({
        'get'   : 'list', 
        'post'  : 'create',
    })),
    path('shop/<str:idx>', ShopViewSet.as_view({
        'get'   : 'retrieve', 
        'put'   : 'update',
        'delete': 'destroy',
    })),
    path('order', OrderViewSet.as_view({
        'get'   : 'list', 
        'post'  : 'create',
    })),
    path('order/<str:idx>', OrderViewSet.as_view({
        'get'   : 'retrieve', 
        'put'   : 'update',
        'delete': 'destroy',
    })),
]