from django.db import models



class Author(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
     
    def __str__(self):
        return f"{self.name}"

    

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=200)
    status=models.BooleanField(default=False,verbose_name='Completed')
    created_at=models.DateField(auto_now_add=True)
    due_date=models.DateField()
    author=models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
        return f"Title:{self.title}\n\nDescription:{self.description}"

