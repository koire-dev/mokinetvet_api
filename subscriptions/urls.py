from django.urls import path
from subscriptions.views import SubscriptionViewSet

urlpatterns = [
    # Création d’un abonnement
    path('subscriptions/create/', SubscriptionViewSet.as_view({'post': 'create'}), name='subscription-create'),

    # Liste des abonnements (admin) ou abonnements de l’utilisateur (éleveur)
    path('subscriptions/', SubscriptionViewSet.as_view({'get': 'list'}), name='subscription-list'),

    # Détail d’un abonnement
    path('subscriptions/<int:pk>/', SubscriptionViewSet.as_view({'get': 'retrieve'}), name='subscription-detail'),

    # Mise à jour complète
    path('subscriptions/<int:pk>/update/', SubscriptionViewSet.as_view({'put': 'update'}), name='subscription-update'),

    # Mise à jour partielle
    path('subscriptions/<int:pk>/partial-update/', SubscriptionViewSet.as_view({'patch': 'partial_update'}), name='subscription-partial-update'),

    # Suppression
    path('subscriptions/<int:pk>/delete/', SubscriptionViewSet.as_view({'delete': 'destroy'}), name='subscription-delete'),

    # Abonnement actif de l’utilisateur connecté
    path('subscriptions/my-subscription/', SubscriptionViewSet.as_view({'get': 'my_subscription'}), name='subscription-my'),
]
