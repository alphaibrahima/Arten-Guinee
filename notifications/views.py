from django.shortcuts import redirect, render
from notifications.models import Notification


# from django.template import loader
# from django.http import HttpResponse




def ShowNotifications(request):
    user = request.user
    notifications = Notification.objects.filter(user=user, is_seen=False).order_by('-date')
    # Notification.objects.filter(user=user, is_seen=False).update(is_seen=True)

    context = {
        'notifications': notifications
    }

    return render(request, 'notifications/notifications.html', context)



def DeleteNotification(request, noti_id):
    user = request.user
    Notification.objects.filter(id=noti_id, user=user).delete()
    Notification.objects.filter(id=noti_id, user=user).update(is_seen=True)
    return redirect('show-notifications')



def CountNotifications(request):
    count_notifications = None
    if request.user.is_authenticated:
        count_notifications = Notification.objects.filter(user=request.user, is_seen=False).count()
    return {'count_notifications': count_notifications}