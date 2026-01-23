#  auth_app/models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password, check_password

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.email
# ... هنا كود User الحالي عندك ...

class Course(models.Model):
    """
    نموذج يمثل دورة تعليمية داخل المنصة.
    - title: عنوان الدورة
    - description: وصف مختصر
    - level: مستوى الدورة (مبتدئ، متوسط، متقدم مثلاً)
    - owner: المستخدم الذي أنشأ الدورة (المدرّس أو الأدمن)
    - created_at: تاريخ إنشاء الدورة
    """
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    level = models.CharField(
        max_length=20,
        choices=LEVEL_CHOICES,
        default='beginner',
    )
    owner = models.ForeignKey(
        'auth_app.User',           # ربط مع نموذج المستخدم المخصص لديك
        on_delete=models.CASCADE,  # حذف الدورات إذا حُذف صاحبها
        related_name='courses'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']  # أحدث الدورات أولاً في الاستعلامات

    def __str__(self) -> str:
        # تمثيل نصي مفيد داخل لوحة الإدارة والديباغ
        return f"{self.title} ({self.level})"
