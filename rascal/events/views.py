from datetime import datetime
from django.utils import timezone
from django.http import JsonResponse
from rest_framework.decorators import api_view
from events.models import Event, UserEvent
from users.models import User

@api_view(['POST'])
def create_event(request):
    """
    Creates a new event
    """
    try:
        title = request.data['title']
        description = request.data['description']
        start_date = request.data['start_date']
        end_date = request.data['end_date']
        
        start_date = datetime.fromisoformat(start_date.replace("Z", "+00:00"))
        end_date = datetime.fromisoformat(end_date.replace("Z", "+00:00"))

        event = Event.objects.create(
            title=title,
            description=description,
            start_date=start_date,
            end_date=end_date
        )
        return JsonResponse({'message': 'Event created successfully', 'uuid': event.uuid})
    except KeyError as e:
        return JsonResponse({'message': f'Missing field: {str(e)}'}, status=400)
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)


@api_view(['POST'])
def subscribe_event(request, uuid):
    """
    Subscribes a user to an event
    """
    try:
        user_uuid = request.data['user_uuid']
        
        user = User.objects.filter(uuid=user_uuid, is_deleted=False).first()
        if not user:
            return JsonResponse({'message': 'User not found'}, status=404)
            
        event = Event.objects.filter(uuid=uuid, is_deleted=False).first()
        if not event:
            return JsonResponse({'message': 'Event not found'}, status=404)
            
        already_subscribed = UserEvent.objects.filter(user=user_uuid, event=uuid).exists()
        if already_subscribed:
            return JsonResponse({'message': 'User already subscribed to this event'}, status=400)
            
        UserEvent.objects.create(
            user=user_uuid,
            event=uuid
        )
        return JsonResponse({'message': 'User subscribed to event successfully'})
    except KeyError as e:
        return JsonResponse({'message': f'Missing field: {str(e)}'}, status=400)
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)
