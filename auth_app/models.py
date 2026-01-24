#  auth_app/models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password, check_password


class User(models.Model):
    ROLE_CHOICES = [
        ("student", "Student"),
        ("instructor", "Instructor"),
        ("admin", "Admin"),
    ]

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    # بيانات أساسية
    full_name = models.CharField(max_length=150, blank=True)
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="student",
    )
    is_active = models.BooleanField(default=True)

    # إعدادات الحساب
    language = models.CharField(max_length=5, default="ar")  # ar / en
    timezone = models.CharField(max_length=50, default="Asia/Amman")

    # التتبع الزمني
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='deleted_users',
    )
    # دوال الباسورد
    def set_password(self, raw_password: str) -> None:
        self.password = make_password(raw_password)

    def check_password(self, raw_password: str) -> bool:
        return check_password(raw_password, self.password)

    def __str__(self) -> str:
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
