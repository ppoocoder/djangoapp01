from django.urls import path
from boss import views 


urlpatterns = [
    path('orders/<int:shop_id>', views.order_list, name="order_list"),
    path('timeinput/', views.time_input, name="timeinput"),
]