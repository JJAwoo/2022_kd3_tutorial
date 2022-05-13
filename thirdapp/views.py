from django.http import HttpResponse
from django.shortcuts import render
from django.db import models
from django.db.models.fields import CharField, IntegerField, DateField, FloatField


# Create your views here.

from django.shortcuts import render
from .models import JejuOlle, Shop, Owner

def shop(request):
    shop_list = Shop.objects.all()
    return render(
    request,
    'thirdapp/shop.html',
    {'shop_list': shop_list}
)

def jeju_olle(request):
    # jeju_olle_list = JejuOlle.objects.all()

    time = request.GET.get('time')

    if not time :
        time = ''

    jeju_olle_list = JejuOlle.objects.filter(
        time_info__contains = time)

    return render(
    request,
    'thirdapp/jeju_olle.html',
    {'jeju_olle_list': jeju_olle_list}
)

def jeju_olle_ajax(request):
    return render(request,
     'thirdapp/jeju_olle_ajax.html',
     {} )

def owner(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        owner = Owner(name=name)
        owner.save()
       #result = '%s ' % (name)
       #return HttpResponse(result)
       #owner.name += result 
    return render(request, 'thirdapp/post.html')


