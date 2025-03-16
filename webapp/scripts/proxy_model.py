from ..models import Task, TaskStatus, CompletedTask, TODOTask

def run():
    # completedTask = TaskStatus.COMPLETED
    # tasks = Task.objects.filter(status=completedTask)


    tasks = TODOTask.objects.all()

    print(tasks)