
from django.core.paginator import Paginator
from django.shortcuts import render

from goods.models import Categories, Products
from goods.utils import q_search

# Create your views here.

def catalog(request,category_slug=None):
    
    page=request.GET.get('page', 1)
    onpage=request.GET.get('onpage',)
    sorted=request.GET.get('sorted',)
    query=request.GET.get('search',)
    brands=request.GET.get('brands',)
    color=request.GET.get('color',)
    country=request.GET.get('country',)
    
    
    if category_slug=='all':
        goods=Products.objects.all()
        title='Все товары'
    elif query:
        goods=q_search(query)
        title=query
    else:
        goods=Products.objects.filter(category__slug=category_slug)
        title=Categories.objects.filter(slug=category_slug).first()

         

    if brands:
        goods=goods.filter(brand=brands)
    
    if color:
        goods=goods.filter(color=color)
    
    if country:
        goods=goods.filter(country=country)


    if sorted == 'price_desc':
        goods=goods.order_by('-price')
    elif sorted == 'price_asc':
        goods=goods.order_by('price')


    if onpage:
        paginator=Paginator(goods,int(onpage))
        current_page=paginator.page(int(page))
            
    else:
        paginator=Paginator(goods,1)
        current_page=paginator.page(int(page))
    
    current_url = request.path

    context={
        'title': title,
        'goods':current_page,
        'slug_url':category_slug,
        'onpage':onpage,
        'current_url':current_url,
        
}

    return render(request,'goods/catalog.html',context)



def product(request,product_slug):

    product=Products.objects.get(slug=product_slug)
    goods=Products.objects.all()[:4]

    context={
        'product':product,
        'sub_title':product.name,
        'goods':goods,
    }

    return render(request,'goods/product.html',context=context)