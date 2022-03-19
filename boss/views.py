from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from order.models import Shop, Menu, Order, Orderfood 
from order.serializers import ShopSerializer ,MenuSerializer
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser 


# Create your views here.
@csrf_exempt
def order_list(req, shop_id):
    if req.method == 'GET':
       order_list = Order.objects.filter(shop=shop_id)
       return render(req, 'boss/order_list.html',{'order_list': order_list})
    else:
       return JsonResponse(status=404)  

@csrf_exempt
def time_input(req):   
    if req.method == 'POST':
         order_item = Order.objects.get(pk=int(req.POST['order_id']))
         shop_id= order_item.shop.id
         print(shop_id)
         order_item.estimated_time = int(req.POST['estimated_time'])
         order_item.save()
         return render(req, 'boss/success.html',{'shop_id':int(shop_id)})
    else:
       return JsonResponse(status=404)