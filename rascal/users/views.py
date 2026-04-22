from django.http import JsonResponse
from rest_framework.decorators import api_view
from users.models import User, UserType

@api_view(['POST'])
def register_user(request):
    """
    Registers a new user
    """
    full_name = request.data['full_name']
    email = request.data['email']
    dob = request.data['dob']
    password = request.data['password']
    
    User.objects.create(full_name=full_name, email=email, dob=dob, password=password, user_type=UserType.MEMBER)
    return JsonResponse({'message': 'User created successfully'})


@api_view(['POST'])
def register_admin(request):
    """
    Registers an admin user with the given credentials
    """
    full_name = request.data['full_name']
    email = request.data['email']
    dob = request.data['dob']
    password = request.data['password']
    
    User.objects.create(full_name=full_name, email=email, dob=dob, password=password, user_type=UserType.ADMIN)
    return JsonResponse({'message': 'Admin created successfully'})

@api_view(['POST'])
def login_user(request):
    """
    Returns user's uuid on login if credentials are correct
    """
    email = request.data.get('email', None)
    password = request.data.get('password', None)
    if not email or not password:
        return JsonResponse({'message': 'Email and password are required'}, status=400)

    user = User.objects.filter(email=email, password=password, is_deleted=False).first()
    if not user:
        return JsonResponse({'message': 'User not found'}, status=404)
    return JsonResponse({'uuid': user.uuid})


    