from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from .models import Course
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