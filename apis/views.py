# Import the viewsets module from Django REST Framework
from rest_framework import viewsets

# Import the local serializers and models
from .serializers import CarSerializer, DealerSerializer, SalesSerializer
from .models import Car, Dealer, Sales

# Create a viewset for the Car model
class CarViewSet(viewsets.ModelViewSet):
    # Define the queryset to retrieve all Car objects
    queryset = Car.objects.all()
    # Specify the serializer to be used for Car serialization
    serializer_class = CarSerializer

# Create a viewset for the Dealer model
class DealerViewSet(viewsets.ModelViewSet):
    # Define the queryset to retrieve all Dealer objects
    queryset = Dealer.objects.all()
    # Specify the serializer to be used for Dealer serialization
    serializer_class = DealerSerializer

# Create a viewset for the Sales model
class SalesViewSet(viewsets.ModelViewSet):
    # Define the queryset to retrieve all Sales objects
    queryset = Sales.objects.all()
    # Specify the serializer to be used for Sales serialization
    serializer_class = SalesSerializer

    def get_queryset(self):
        # Override the get_queryset() method to customize the queryset based on query parameters
        queryset = super().get_queryset()
        query_params = self.request.query_params
        if "car_id" in query_params and query_params.get("car_id"):
            queryset = queryset.filter(car=query_params.get("car_id"))
        elif "dealer_id" in query_params and query_params.get("dealer_id"):
            queryset = queryset.filter(dealer=query_params.get("dealer_id"))
        else:
            queryset = queryset.order_by('-created_at')
        return queryset
