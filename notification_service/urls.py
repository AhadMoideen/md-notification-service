from django.urls import path

from .views import UserNotificationAPIView, RestaurantNotificationAPIView

urlpatterns = [
    path('notification/', UserNotificationAPIView.as_view()),
    path('notification/user/<str:email>', UserNotificationAPIView.as_view()),
    path('notification/restaurant/<str:restaurantId>', RestaurantNotificationAPIView.as_view()),
    path('notification/restaurant/<str:restaurantId>/status', RestaurantNotificationAPIView.as_view())
]
