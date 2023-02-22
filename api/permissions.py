
from rest_framework.permissions import IsAuthenticated

class AllowOptionsAuthentication(IsAuthenticated):
    def has_permission(self, request, view):
        if request.method:
            return True
        return request.user and request.user.is_authenticated
