from django.contrib import admin
from .models import Task  # Assuming you have a Task model in models.py

admin.site.register(Task)  # Register the Task model with the admin site