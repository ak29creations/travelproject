from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render
from . models import Place,Team


def demo(request):
    # return HttpResponse("Hello World") To print Hello World
    # return render(request,'home.html',{'name':'AK Creations'})To display html page
    place = Place.objects.all()
    team = Team.objects.all()
    return render(request,'index.html',{'place' : place,'team':team})
# def about(request):
#     return render(request, 'about.html')
#
# def contact(request):
#     return HttpResponse("am contact page")

# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request, 'result.html',{'result':res})