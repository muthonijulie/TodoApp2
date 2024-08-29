from django import template

register=template.Library()
register.filter(name='task_status')
def task_status(value):
    if value:
        return "Completed"
    else:
        return "Pending "