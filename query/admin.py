from django.contrib import admin
from .models import Section,Lecture,Course
# Register your models here.
admin.site.register(Section)
admin.site.register(Lecture)
admin.site.register(Course)