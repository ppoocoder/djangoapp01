from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from order.models import Shop, Menu, Order, Orderfood 
from order.serializers import ShopSerializer ,MenuSerializer
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser 


# Create your views here.
@csrf_exempt
def order_list(req):
    if req.method == 'GET':
       order_list = Order.objects.all()
       return render(req, 'delivery/order_list.html',{'order_list': order_list})

    elif req.method == 'POST':
         order_item = Order.objects.get(pk=int(req.POST['order_id']))
         order_item.deliver_finish=1
         order_item.save()
         return render(req, 'delivery/success.html')
