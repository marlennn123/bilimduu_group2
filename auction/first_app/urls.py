from django.urls import path, include
from .views import CarViewSet, BetViewSet

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('cars/', CarViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'}), name='cars_list'),
    path('bets/', BetViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'}), name='bets_list')
]