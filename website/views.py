from django.shortcuts import render

# Create your views here.

def spl(request):
    context = {}
    return render(request, 'website/splhome.html', context)

def spl1(request):
    context = {}
    return render(request, 'website/splproducts.html', context)

def spl2(request):
    context = {}
    return render(request, 'website/splpeople.html', context)
    
def spl3(request):
    context = {}
    return render(request, 'website/splcontactus.html', context)