from flask import request
from rest_framework import permissions
from sqlalchemy import true


class UddateOwnProfile(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return true
        return obj.id == request.user.id