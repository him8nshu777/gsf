from django.urls import path
from conversation import views
urlpatterns = [
    path('postMessage',views.postMessage, name='postMessage'),
    path('employee_home',views.employee_home, name='employee_home'),
    path('employee_chat/<str:customer_username>/', views.employee_chat, name='employee_chat'),
]
