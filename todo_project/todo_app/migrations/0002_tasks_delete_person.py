# Generated by Django 5.0.7 on 2024-08-26 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200)),
                ('status', models.BooleanField(default=False, verbose_name='Completed')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('due_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
