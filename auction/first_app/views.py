from django.shortcuts import render
from .serializers import CarSerializer, BetSerializer
from rest_framework import viewsets
from .models import Car, Bet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination


class Pagination(PageNumberPagination):
    page_size_query_param = 'page_number'
    page_size = 10
    max_page_size = 100

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', "year", "country"]
    search_fields = ['marka', 'model']
    ordering_fields = ['price', "year"]

class BetViewSet(viewsets.ModelViewSet):
    queryset = Bet.objects.all()
    serializer_class = BetSerializer
    pagination_class = PageNumberPagination