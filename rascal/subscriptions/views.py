# from .serializers import AddSubscriptionPlanSerializer
from django.utils import timezone
from django.http import JsonResponse
from rest_framework.decorators import api_view
from users.models import User
from subscriptions.models import UserSubscription, SubscriptionPlan, SubscriptionDuration
from subscriptions.serializers import *


@api_view(['POST'])
def add_subscription_plan(request):
    """
    Adds a subscription plan
    """
    try:
        serializer = AddSubscriptionPlanSerializer(data=request.data)
        if serializer.is_valid():
            subscription_plan = SubscriptionPlan.objects.filter(
                name=serializer.validated_data['name'],
                plan_type=serializer.validated_data['plan_type'],
            ).first()
            if subscription_plan:
                return JsonResponse({'message': 'Subscription plan already exists'}, status=400)
            subscription_plan = SubscriptionPlan.objects.create(
                name=serializer.validated_data['name'],
                plan_type=serializer.validated_data['plan_type'],
                description=serializer.validated_data['description'],
                price=serializer.validated_data['price'],
                duration=serializer.validated_data['duration'],
            )
            return JsonResponse({'message': 'Subscription plan added successfully'})
        else:
            print(serializer.errors)
            return JsonResponse(serializer.errors, status=400)
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)


@api_view(['GET'])
def get_all_subscription_plans(request):
    """
    Returns all subscription plans
    """
    subscription_plans = SubscriptionPlan.objects.all()
    serializer = AllSubscriptionPlanSerializer(subscription_plans, many=True)
    return JsonResponse({'plans': serializer.data})

@api_view(['POST'])
def subscribe(request, plan):
    """
    Creates a subscription for a user
    """
    user = User.objects.filter(uuid=request.data['user_uuid'], is_deleted=False).first()
    if not user:
        return JsonResponse({'message': 'User not found'}, status=404)

    subscription_plan = SubscriptionPlan.objects.filter(uuid=plan).first()
    if not subscription_plan:
        return JsonResponse({'message': 'Subscription plan not found'}, status=404)
    end_date = timezone.now() + timezone.timedelta(days=30) if subscription_plan.duration == SubscriptionDuration.MONTHLY else timezone.now() + timezone.timedelta(days=365)

    try:
      UserSubscription.objects.filter(user=user.uuid).delete()
    except Exception as e:
      pass
    subscription = UserSubscription.objects.create(
        user=user.uuid,
        plan=subscription_plan,
        start_date=timezone.now(),
        end_date=end_date,
    )
    serializer = UserSubscriptionSerializer(subscription)
    return JsonResponse({'subscription': serializer.data})

@api_view(['GET'])
def my_subscription(request, uuid):
    """
    Returns the subscription of the user with the given uuid
    """
    user = User.objects.filter(uuid=uuid, is_deleted=False).first()
    if not user:
        return JsonResponse({'message': 'User not found'}, status=404)

    user_subscription = UserSubscription.objects.filter(user=user).first()
    if not user_subscription:
        return JsonResponse({'message': 'User not found'}, status=404)

    serializer = UserSubscriptionSerializer(user_subscription)
    return JsonResponse(serializer.data)
