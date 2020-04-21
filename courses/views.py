from django.shortcuts import get_object_or_404, render

from .models import Course 
from categories.models import Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):   
    courses = Course.objects.filter(is_published=True)
    paginator = Paginator(courses, 10)
    page_number = request.GET.get('page')
    page_courses = paginator.get_page(page_number)
    categories = Category.objects.all()
    context = {'courses': page_courses, 'categories':categories}
    return render(request, 'courses/courses.html', context)

  

def course (request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    context = {'course' : course}
    return render(request, 'courses/course.html', context)

def search (request):   
   categories = Category.objects.all()  
   courses = Course.objects.filter(is_published=True)

   #keyword
   if 'Instructor' in request.GET:  
       instructor = request.GET['instructor']
       courses= courses.filter(instructor__icontains=instructor)
   if 'subject' in request.GET:  
       subject = request.GET['subject'] 
       courses= courses.filter(title__icontains=subject) 
   if 'level' in request.GET:  
       level = request.GET['level'] 
       courses= courses.filter(category_id=level)  

   paginator = Paginator(courses, 10)
   page_number = request.GET.get('page')
   page_courses = paginator.get_page(page_number)
   
   context = {
       'courses': page_courses,
       'categories':categories,
       'values': request.GET}  
   return render(request, 'pages/index.html', context)