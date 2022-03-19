from django.urls import path
from order import views 


urlpatterns = [
    path('shops/', views.shop, name="shops"),
    path('menus/<int:shop_id>', views.menu, name="menus"),
    path('order/', views.order, name="order") 
]