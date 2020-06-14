from django.shortcuts import render
# Create your views here.
def MyTempView(request):
    return render(request,'Welcome.html')
def Thanks_Page(request):
    return render(request,'Thanks.html')