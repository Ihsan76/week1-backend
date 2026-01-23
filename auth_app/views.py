# auth_app/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .models import User, Course
from .serializers import UserSerializer, CourseSerializer

# ... register, login, get_users, delete_user كما هي ...

@api_view(['POST'])
def register(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    if not email or not password:
        return Response(
            {'error': 'Email and password are required'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    if len(password) < 6:
        return Response(
            {'error': 'Password must be at least 6 characters'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    if User.objects.filter(email=email).exists():
        return Response(
            {'error': 'User already exists'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    user = User(email=email)
    user.set_password(password)
    user.save()
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    if not email or not password:
        return Response(
            {'error': 'Email and password are required'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    try:
        user = User.objects.get(email=email)
        if user.check_password(password):
            serializer = UserSerializer(user)
            return Response({
                'success': True,
                'user': serializer.data
            })
        else:
            return Response(
                {'error': 'Invalid credentials'},
                status=status.HTTP_401_UNAUTHORIZED
            )
    except User.DoesNotExist:
        return Response(
            {'error': 'Invalid credentials'},
            status=status.HTTP_401_UNAUTHORIZED
        )

@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        return Response({'success': True, 'message': 'User deleted'})
    except User.DoesNotExist:
        return Response(
            {'error': 'User not found'},
            status=status.HTTP_404_NOT_FOUND
        )

# ... register, login, get_users, delete_user كما هي ...

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])  # لاحقاً يمكن تقييدها بالمصادقة
def courses_list_create(request):
    """
    GET: إرجاع قائمة بجميع الدورات.
    POST: إنشاء دورة جديدة.
    في هذه المرحلة نسمح لأي شخص بالوصول (AllowAny),
    لاحقاً يمكن ربطها بالمستخدم المسجل فقط.
    """
    if request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        # مؤقتاً، نربط صاحب الدورة بأول مستخدم في النظام أو مستخدم ثابت
        # لاحقاً: نستخدم المستخدم الحالي من الـ auth (JWT / Session)
        owner = User.objects.first()
        if owner is None:
            return Response(
                {'error': 'No owner user found to attach to the course.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            course = serializer.save(owner=owner)
            return Response(
                CourseSerializer(course).data,
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def course_delete(request, course_id: int):
    """
    DELETE: حذف دورة حسب الـ id.
    في المستقبل يمكن التأكد أن الطالب/المدرس صاحب الحق هو من يحذف.
    """
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return Response(
            {'error': 'Course not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    course.delete()
    return Response({'success': True, 'message': 'Course deleted'})
