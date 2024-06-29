from django.shortcuts import render, redirect
from django.views import View
from .models import Chat, UserProfile
from django.urls import reverse


# Create your views here.

from django.db.models import Q  # Import the Q object

def postMessage(request):
    current_user_profile = UserProfile.objects.get(user=request.user)

    if request.method == "POST":
        text = request.POST.get("text")
        if text:
            sender_profile = UserProfile.objects.get(user=request.user)
            chat_text = Chat(content=text, sender=sender_profile, receiver=None)
            chat_text.save()
            return redirect(reverse('postMessage')) 

    # texts = Chat.objects.filter(sender=request.user.userprofile)
    texts = Chat.objects.filter(Q(sender=current_user_profile) | Q(receiver=current_user_profile))
    return render(request, 'customer_chat.html', {'texts': texts})

def employee_chat(request, customer_username):
    # Find the customer UserProfile by username
    customer_profile = UserProfile.objects.get(user__username=customer_username)
    sender_profile = UserProfile.objects.get(user=request.user)
    if request.method == "POST":
        text = request.POST.get("text")
        if text:
            sender_profile = UserProfile.objects.get(user=request.user)
            chat_text = Chat(content=text, sender=sender_profile, receiver=customer_profile)
            chat_text.save()
            return redirect(reverse('employee_chat',args=[customer_profile]))

    chat_messages = Chat.objects.filter(Q(sender=sender_profile, receiver=customer_profile) | Q(sender=customer_profile))

    return render(request, 'employee_chat.html', {'chat_messages': chat_messages, 'customer_profile': customer_profile, 'customer_username': customer_username})

def employee_home(request):
    # Fetch customer usernames who have sent messages
    customers_with_messages = Chat.objects.filter(sender__is_customer=True).values('sender__user__username').distinct()
    print(customers_with_messages)
    return render(request, 'employee_home.html', {'customers_with_messages': customers_with_messages})
   