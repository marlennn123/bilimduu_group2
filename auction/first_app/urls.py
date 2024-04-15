from django.urls import path
from .views import CarViewSet, BetViewSet

urlpatterns = [
    path('cars/', CarViewSet.as_view({'get':'list', 'post':'create', 'put':'update', 'delete':'destroy'}), name='cars-list'),
    path('bets/', BetViewSet.as_view({'get':'list', 'post':'create', 'put':'update', 'delete':'destroy'}), name='cars-list')
]