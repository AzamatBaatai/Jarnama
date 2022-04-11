from rest_framework.permissions import BasePermission


class IsAuthor(BasePermission):
    # #rabotaet nad neskolkimi obyektami (create, list)
    # def has_permission(self, request, view):
    #     pass

    #rabota s odnim obyektom(retrieve, update, destroy)
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and obj.author == request.user
