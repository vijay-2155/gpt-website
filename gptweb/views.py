from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'homepage.html')
def dcme(request):
    return render(request,'cme.html')
def deee(request):
    return render(request,'eee.html')
def dce(request):
    return render(request,'civil.html')
def dmec(request):
    return render(request,'dmec.html')

def ccp(request):
    return render(request,'ccp.html')

# administration
def ccp_fac(request):
    return render(request,'staff_ccp.html')
def dcme_fac(request):
    return render(request,'staff_dcse.html')
def dme_fac(request):
    return render(request,'staff_dme.html')
def dce_fac(request):
    return render(request,'staff_dce.html')
def deee_fac(request):
    return render(request,'staff_deee.html')