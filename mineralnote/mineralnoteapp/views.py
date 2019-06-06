from django.shortcuts import render, get_object_or_404
from .models import ProductType, Product, Review
from .forms import ProductForm

# Create your views here.

def index (request):
    return render(request, 'mineralnoteapp/index.html')

def gettypes(request):
    type_list=ProductType.objects.all()
    return render(request, 'mineralnoteapp/types.html' ,{'type_list' : type_list})

def getresource(request):
    products_list=Product.objects.all()
    return render(request, 'mineralnoteapp/resource.html', {'products_list': products_list})

def resourcedetails(request, id):
    res=get_object_or_404(Product, pk=id)
    discount=res.memberdiscount
    reviews=Review.objects.filter(product=id).count()
    context={
        'res' : res,
        'discount' : discount,
        'reviews' : reviews,
    }
    return render(request, 'mineralnoteapp/resourcedetails.html', context=context)

def newProduct(request):
     form=ProductForm
     if request.method=='POST':
          form=ProductForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ProductForm()
     else:
          form=ProductForm()
     return render(request, 'mineralnoteapp/newresource.html', {'form': form})