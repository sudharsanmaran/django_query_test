from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class Section(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    dummy_course = models.ForeignKey(Course,related_name="dummy_set", on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    order = models.IntegerField()
    def __str__(self):
        return self.title


"""related_name"""
# >>> from query.models import Section, Lecture, Course
# >>> m = Course.objects.get(title="math")
# >>> m.section_set.all()
# <QuerySet [<Section: math_course>]>
# >>> m.dummy_set.all()
# <QuerySet [<Section: sci_course>]>
# >>>

class Lecture(models.Model):
    section = models.ForeignKey(Section,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    order = models.IntegerField()
    code_link = models.CharField(max_length=100,blank=True,null=True)
    slug = models.CharField(max_length=200)
    def __str__(self):
        return self.title