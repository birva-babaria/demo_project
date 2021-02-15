from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
	return render(request,'home.html',{'name':'birva'})

def add(request):
	n1 = int(request.POST['a'])
	n2 = int(request.POST['b'])
	res = n1+n2
	return render(request,'result.html',{'result':res})