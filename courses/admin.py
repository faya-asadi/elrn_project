from django.contrib import admin

from .models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'instructor', 'is_published']
    list_filter = ['instructor',]
    list_editable = ['is_published',]
    search_fields = ['title', 'description',]
    list_per_page = 25
   # list_display_link = ('id', 'title')


admin.site.register(Course, CourseAdmin)

