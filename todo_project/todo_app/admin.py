from django.contrib import admin
from django.forms import Textarea
from .models import Task,Author
from django.db import models

class TaskModel(admin.ModelAdmin):
    list_display=['title','description','status']
    list_filter=['author','due_date']
    search_fields=['status','title','author','due_date']
    formfield_overrides={
        models.TextField:{
            'widget':Textarea(attrs={
                'rows':4,
                'cols':6
            } )
        }
    }

    def mark_as_completed(self,request,queryset):
        queryset.update(status=1)
    mark_as_completed.short_description='Mark selected tasks as completed'
    actions=['mark_as_completed']
# Register your models here.
admin.site.register(Task,TaskModel)
admin.site.register(Author)

admin.site.site_header='Tasker App'
admin.site.site_title='Taskers'