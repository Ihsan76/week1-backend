#  auth_app/serializers.py

from rest_framework import serializers
from .models import User, Course

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'created_at']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'created_at']
        extra_kwargs = {
            'password': {'write_only': True},
        }

class CourseSerializer(serializers.ModelSerializer):
    """
    Serializer لتحويل كائن Course إلى JSON والعكس.
    نعرض owner كـ رقم (id) فقط في هذه المرحلة لتبسيط الواجهة.
    """
    owner_id = serializers.IntegerField(source='owner.id', read_only=True)

    class Meta:
        model = Course
        fields = [
            'id',
            'title',
            'description',
            'level',
            'owner_id',
            'created_at',
        ]
        read_only_fields = ['id', 'owner_id', 'created_at']
