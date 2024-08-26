from django.shortcuts import render,get_object_or_404,redirect
from .models import Category,Product,Image
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Q

# Create your views here.
def product(request):
    q=Product.objects.order_by('create_date')
    page=request.GET.get('page',1)
    paginator=Paginator(q,12)

    try:
        products=paginator.page(page)
    except EmptyPage:
        products.paginator.page(1)
    except PageNotAnInteger:
        products=paginator.page(1)
        return redirect ('home')
       
        
    
    context={
        'products':products,
        'paginator':paginator
        

    }
    return render(request,'home.html',context)




def product_details(request,slug):
    product=get_object_or_404(Product,slug=slug)
    images=Image.objects.filter(product=product)
    context={
        'product':product,
        'images':images
        

    }
    return render(request,'product_details.html',context)