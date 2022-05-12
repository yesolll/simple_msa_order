from rest_framework import viewsets

class ShopViewSet(viewsets.ViewSet):
    def list(self, request): # /api/shop
        pass
    
    def retrieve(self, request): # /api/shop
        pass
    
    def create(self, request, pk=None): # /api/shop/<str:idx>
        pass
    
    def update(self, request, pk=None): # /api/shop/<str:idx>
        pass
    
    def destroy(self, request, pk=None): # /api/shop/<str:idx>
        pass

class OrderViewSet(viewsets.ViewSet):
    def list(self, request): # /api/order
        pass

    def retrieve(self, request): # /api/order
        pass

    def create(self, request, pk=None): # /api/order/<str:idx>
        pass

    def update(self, request, pk=None): # /api/order/<str:idx>
        pass

    def destroy(self, request, pk=None): # /api/order/<str:idx>
        pass

