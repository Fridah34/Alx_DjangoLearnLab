from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from .serializers import NotificationSerializer
from .models import Notification

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def list_notifications(request):
    user = request.user
    notifications = Notification.objects.filter(recipient=user).order_by('-timestamp')
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def mark_notification_read(request, pk):
    # mark a single notification as read
    notif = get_object_or_404(Notification, pk=pk, recipient=request.user)
    notif.read = True
    notif.save()
    return Response({'detail': 'Marked as read'}, status=200)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def mark_all_read(request):
    Notification.objects.filter(recipient=request.user, read=False).update(read=True)
    return Response({'detail': 'All notifications marked as read'}, status=200)
