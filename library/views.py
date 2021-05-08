from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request,'home.html')

def it_sems(request):
	return render(request,'it_sems.html') 

def cse_sems(request):
	return render(request,'cse_sems.html') 

def ece_sems(request):
	return render(request,'ece_sems.html') 

def eee_sems(request):
	return render(request,'eee_sems.html')

def it_sem1(request):
	return render(request,'it_sem1.html') 

def it_sem2(request):
	return render(request,'it_sem2.html')  

def it_sem3(request):
	return render(request,'it_sem3.html') 

def it_sem4(request):
	return render(request,'it_sem4.html') 

def it_sem5(request):
	return render(request,'it_sem5.html') 

def it_sem3_DMA(request):
	return render(request,'it_sem3_DMA.html') 

