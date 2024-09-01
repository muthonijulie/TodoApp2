from django.db import models

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=200)
    status=models.BooleanField(default=False,verbose_name='Completed')
    created_at=models.DateField(auto_now_add=True)
    due_date=models.DateField()

    def __str__(self):
        return f"Title:{self.title}\nStatus{self.status}"

class author(models.Model):
    