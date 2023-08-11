from django.shortcuts import render

from apps.store.models import Product, Category

def frontpage(request):
   
    featured_categories = Category.objects.all()
  

    context = {
        'featured_categories': featured_categories,
    }

    return render(request, 'frontpage.html', context)

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')