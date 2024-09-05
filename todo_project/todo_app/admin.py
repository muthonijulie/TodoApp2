from django.contrib import admin
from .models import Task,Author

class TaskModel(admin.ModelAdmin):
    list_display=['title','description','status']
    search_fields=['status','title']

# Register your models here.
admin.site.register(Task,TaskModel)
admin.site.register(Author)