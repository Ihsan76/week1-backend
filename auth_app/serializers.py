# auth_app/serializers.py

from rest_framework import serializers
from .models import User, Course


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer كامل لاستخدامات الإدارة / اللوحات الداخلية.
    يحتوي على جميع الحقول بما فيها password (للـ write_only).
    """
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "full_name",
            "role",
            "is_active",
            "language",
            "timezone",
            "created_at",
            "updated_at",
            "password",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }


class UserPublicSerializer(serializers.ModelSerializer):
    """
    Serializer مختصر للـ frontend (login / register / profile).
    لا يعرض كلمة المرور أو الحقول غير الضرورية للواجهة.
    """
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "full_name",
            "role",
            "language",
            "timezone",
            "created_at",
        ]


class CourseSerializer(serializers.ModelSerializer):
    """
    Serializer لتحويل كائن Course إلى JSON والعكس.
    نعرض owner كـ رقم (id) فقط في هذه المرحلة لتبسيط الواجهة.
    """
    owner_id = serializers.IntegerField(source="owner.id", read_only=True)

    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "description",
            "level",
            "owner_id",
            "created_at",
        ]
        read_only_fields = ["id", "owner_id", "created_at"]
