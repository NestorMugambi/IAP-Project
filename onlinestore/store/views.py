from django.shortcuts import render
from django.shortcuts import redirect
from store.forms import ProductForm
from store.models import Product
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "store/home.html")

def products(request):
    latest_products = Product.objects.order_by('-id')

    return render(request, 'store/products.html', {'latest_products': latest_products})   


def add_product(request):
    form = ProductForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            product = form.save(commit=False)
            
            product.save()
            
            return redirect("products")
    else:
        return render(request, "store/add.html", {"form": form})
    