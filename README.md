# Proxy Models in Django 🚀

## What is a Proxy Model? 🤔  
A **Proxy Model** in Django is a way to create different representations of the same database table **without** modifying its structure. Instead of duplicating data, Proxy Models allow you to customize behavior, add managers, or apply filters while keeping the same underlying table.  

---

## Why Use Proxy Models? 🧐  
✔ **No Extra Database Table** – Proxy Models use the same table as the original model.  
✔ **Custom Querysets** – You can define different default filters using custom managers.  
✔ **Maintainable Code** – Keeps the database schema clean while providing different views of the data.  

---

## Example Code 📌  

### 1️⃣ Define a Base Model (`Task`)
```python
from django.db import models

class TaskStatus(models.IntegerChoices):
    TODO = 1, "To Do"
    IN_PROGRESS = 2, "In Progress"
    COMPLETED = 3, "Completed"

class Task(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=TaskStatus.choices)

    def __str__(self):
        return self.name
```

### 2️⃣ Create Proxy Models
```python
class InProgressTask(Task):
    class Meta:
        proxy = True

    objects = models.Manager()

class TodoTask(Task):
    class Meta:
        proxy = True

    objects = models.Manager()
```
### 3️⃣ Query Using Proxy Models
```python
in_progress_tasks = InProgressTask.objects.all()  
todo_tasks = TodoTask.objects.all()
```
