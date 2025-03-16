from django.db import models


class TaskStatus(models.IntegerChoices):
    IN_PROGRESS = 1
    TODO = 2
    COMPLETED = 3

class Task(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=TaskStatus.choices)


    def __str__(self):
        return self.name
    

class CompletedTask(Task):
    class Meta:
        proxy = True


    def save(self, *args, **kwargs):
        if self._state.adding:
            self.status = TaskStatus.COMPLETED
        super().save(*args, **kwargs)


    class Manager(models.Manager):
        def get_queryset(self) -> models.QuerySet:
            return super().get_queryset().filter(status=TaskStatus.COMPLETED)
        
    objects = Manager()





class TODOTask(Task):
    class Meta:
        proxy = True


    def save(self, *args, **kwargs):
        if self._state.adding:
            self.status = TaskStatus.TODO
        super().save(*args, **kwargs)


    class Manager(models.Manager):
        def get_queryset(self) -> models.QuerySet:
            return super().get_queryset().filter(status=TaskStatus.TODO)
        
    objects = Manager()