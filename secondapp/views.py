from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from .models import ArmyShop, Course
# Create your views here.
def main(request):
    return HttpResponse('<u>Main</u>')

def insert(request):

    # 1-linux 입력
    Course.objects.create(name='데이터 분석', cnt = 30)
    # 2-python 입력
    c = Course(name='데이터 수집', cnt = 20)
    c.save()
    # 3-html/css/js 입력
    Course(name='웹개발', cnt = 25).save()
    # 4-django 입력
    Course(name='인공지능', cnt = 20).save()
    return HttpResponse('데이터 입력 완료')

def show(request):
    course = Course.objects.all()
    # result = ''
    # for c in course:
    #  result += c.name + '<br>' 
    # return HttpResponse(result)
    return render(request, 'secondapp/show.html',
    {'data' : course})

def army_shop(request):
    # shops = ArmyShop.objects.all()    query param을 위해 주석처리했음
    
    #             GET['prd']
    prd = request.GET.get('prd')
    if not prd:       # prd에 값이 없을 경우 , 작동하려면 if not 이 되어야 함
        prd = ''
    shops = ArmyShop.objects.filter(name__contains=prd)
            # 검색 할 땐 __contains로 하는 것이 가장 좋음
    return render(request, 
    'secondapp/army_shop.html',
    {'data': shops})


def army_shop2(request, year, month):



    shops = ArmyShop.objects.filter(year=year,
    month=month)

    return render(request, 
    'secondapp/army_shop.html',
    {'data': shops})


def show_ajax(request):
    return render(request,
     'secondapp/show_ajax.html',
     {} )