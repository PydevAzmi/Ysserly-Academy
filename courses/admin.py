from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Professor)
admin.site.register(Student)
admin.site.register(FileContent)
admin.site.register(VideoContent)
admin.site.register(Course)
admin.site.register(Lecture)
admin.site.register(Request)
admin.site.register(Enrollment)
admin.site.register(Notification)