from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from order.models import Shop, Menu, Order, Orderfood 
from order.serializers import ShopSerializer ,MenuSerializer
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser 


# Create your views here.
@csrf_exempt
def shop(req):
    if req.method == 'GET':
        # shop = Shop.objects.all()
        # serializer = ShopSerializer(shop, many=True)
        # return JsonResponse(serializer.data, safe=False)
        shop = Shop.objects.all()
        return render(req, 'order/shop_list.html',{'shop_list':shop})
         
    elif req.method == 'POST':
        data= JSONParser().parse(req)
        serializer= ShopSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201) 
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def menu(req, shop_id):
    if req.method == 'GET':
        # menu = Menu.objects.filter(shop=shop_id)
        # serializer = MenuSerializer(menu, many=True)
       
        # return JsonResponse(serializer.data, safe=False)
        menu = Menu.objects.filter(shop=shop_id)       
        return render(req, 'order/menu_list.html',{'menu_list':menu, 'shop_id':shop_id})
         
    elif req.method == 'POST':
        data= JSONParser().parse(req)
        serializer= MenuSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201) 
        return JsonResponse(serializer.errors, status=400)

from django.utils import timezone

@csrf_exempt
def order(req):
    if req.method == 'POST':
       address= req.POST['address'] 
       shop_id= req.POST['shop_id']
       food_list = req.POST.getlist('menu')
       order_date=timezone.now()

       shop_item = Shop.objects.get(pk=int(shop_id))
       shop_item.order_set.create(address=address, order_date=order_date)
       
       order_item= Order.objects.get(pk=shop_item.order_set.latest('id').id)
       for food in food_list:
           order_item.orderfood_set.create(food_name=food)
       return render(req, 'order/success.html')
    elif req.method == 'GET':
       order_list= Order.objects.all()
       return render(req, 'order/order_list.html',{'order_list':order_list})