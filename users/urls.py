
from django.urls import path

from users.views import (
    UserCreateView,
    UserListView,
    UserDetailView,
    UserUpdateView,
    UserDeleteView,
    CurrentUserView,
    LogoutView,
    MyTokenObtainPairView, home_view
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('', home_view, name='home'),
    path('register/', UserCreateView.as_view(), name='user-register'),
    path('login/', MyTokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
    path('me/', CurrentUserView.as_view(), name='current-user'),

    # path('admin/', admin.site.urls),
]

