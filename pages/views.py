from django.shortcuts import render
from django.http import HttpResponse
from courses.models import Course 
from categories.models import Category
from courses.choices import levels
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def index(request):
     courses = Course.objects.filter(is_published=True)
     paginator = Paginator(courses, 10)
     page_number = request.GET.get('page')
     page_courses = paginator.get_page(page_number)
     categories = Category.objects.all()
     context = {'courses': page_courses,
     'levels': levels,
     'categories':categories}
     return render(request, 'pages/index.html', context)
     

def about(request):
    return render(request, 'pages/about.html')
