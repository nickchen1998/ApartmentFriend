from afd.celery import app
from tasks.models import Task, Run, Status
from django.utils import timezone
from env_settings import EnvSettings


@app.task()
def period_search_tasks(is_test: bool = False):
    env_settings = EnvSettings()
    tasks = Task.objects.order_by("-created_time")

    for task in tasks:
        run = task.run_set.order_by("-created_time").first()
        if run.status == Status.PENDING and run.start_time < timezone.now():
            celery_id = remove_rentable_task.apply_async()

            run.celery_id = celery_id
            run.save()
        elif run.status == Status.STARTED and (timezone.now() - run.start_time).seconds > env_settings.TASK_TIMEOUT:
            pass


@app.task()
def remove_rentable_task():
    pass


@app.task()
def fetch_rent_data_task():
    pass


@app.task()
def crawler_task():
    pass
