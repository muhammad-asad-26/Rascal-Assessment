from django.urls import path
from subscriptions import views

urlpatterns = [
    path('add', views.add_subscription_plan),
    path('all', views.get_all_subscription_plans),
    path('subscribe/<uuid:plan>', views.subscribe),
    path('me', views.my_subscription),
]