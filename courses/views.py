from django.shortcuts import get_object_or_404, render

from .models import Course 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
   courses = Course.objects.filter(is_published=True)
   paginator = Paginator(courses, 10)
   page_number = request.GET.get('page')
   page_courses = paginator.get_page(page_number)
   context = {'courses': page_courses}
   return render(request, 'courses/courses.html', context)


def course (request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    context = {'course' : course}
    return render(request, 'courses/course.html', context)

def search (request):    
    return render(request, 'courses/search.html')