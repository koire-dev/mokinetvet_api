from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'


class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.role == 'admin'


class IsOwnerOrReadOnly(BasePermission):
    """
    Seul l'utilisateur qui a créé l'objet (ex: animal) peut le modifier ou le supprimer.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user


class IsVet(BasePermission):
    """
    Autorise uniquement les vétérinaires.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'veterinaire'


class IsFarmer(BasePermission):
    """
    Autorise uniquement les éleveurs.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'eleveur'


class IsFarmerOrVet(BasePermission):
    """
    Autorise les éleveurs et vétérinaires.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['eleveur', 'veterinaire']


class IsConsultationParticipant(BasePermission):
    """
    Vérifie que l'utilisateur est lié à la consultation (éleveur ou vétérinaire).
    """
    def has_object_permission(self, request, view, obj):
        return request.user == obj.animal.user or request.user == obj.vet


class IsMessageParticipant(BasePermission):
    """
    Vérifie que l'utilisateur participe à la conversation (sender ou receiver).
    """
    def has_object_permission(self, request, view, obj):
        return request.user == obj.sender or request.user == obj.receiver


class IsOwnerOfAnimal(BasePermission):
    """
    Vérifie que l'utilisateur est le propriétaire de l'animal.
    """
    def has_object_permission(self, request, view, obj):
        return obj.animal.user == request.user
