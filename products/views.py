from django.shortcuts import render

# Create your views here.


def watercurls(request):
    return render(request, "products/watercurls.html")
def bonestraight(request):
    return render(request, "products/bonestraight.html")
def pinkycurls(request):
    return render(request, "products/pinkycurls.html")  
def products(request):
    return render(request, "products/products.html")