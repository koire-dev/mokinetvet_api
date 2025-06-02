from django.urls import path
from animals.views import AnimalViewSet

urlpatterns = [
    # Ajouter un nouvel animal
    path('animals/create/', AnimalViewSet.as_view({'post': 'create'}), name='animal-create'),

    # Liste des animaux enregistrés par l’éleveur connecté
    path('animals/mine/', AnimalViewSet.as_view({'get': 'mes_animaux'}), name='animal-mine'),

    # Détail d’un animal spécifique (accessible uniquement à l’éleveur propriétaire)
    path('animals/<int:pk>/', AnimalViewSet.as_view({'get': 'retrieve'}), name='animal-detail'),

    # Mise à jour complète d’un animal
    path('animals/<int:pk>/update/', AnimalViewSet.as_view({'put': 'update'}), name='animal-update'),

    # Mise à jour partielle (facultatif mais utile)
    path('animals/<int:pk>/partial-update/', AnimalViewSet.as_view({'patch': 'partial_update'}), name='animal-partial-update'),

    # Suppression d’un animal
    path('animals/<int:pk>/delete/', AnimalViewSet.as_view({'delete': 'destroy'}), name='animal-delete'),
]
