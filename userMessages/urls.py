from django.urls import path
from userMessages.views import MessageViewSet

urlpatterns = [
    path('userMessages/create/', MessageViewSet.as_view({'post': 'create'}), name='message-create'),
    path('userMessages/', MessageViewSet.as_view({'get': 'list'}), name='message-list'),
    path('userMessages/<int:pk>/', MessageViewSet.as_view({'get': 'retrieve'}), name='message-detail'),
    path('userMessages/<int:pk>/update/', MessageViewSet.as_view({'put': 'update'}), name='message-update'),
    path('userMessages/<int:pk>/partial-update/', MessageViewSet.as_view({'patch': 'partial_update'}), name='message-partial-update'),
    path('userMessages/<int:pk>/delete/', MessageViewSet.as_view({'delete': 'destroy'}), name='message-delete'),
]
