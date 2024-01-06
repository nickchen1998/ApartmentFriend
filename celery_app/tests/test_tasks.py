from django.test import TestCase
from django.utils import timezone
from tasks.models import Task, Run, Status, Frequency
from celery_app.tasks import system_tasks


class CeleryAppTestCase(TestCase):
    def setUp(self) -> None:
        frequency = Frequency.objects.create(days=0, hours=0, minutes=0, seconds=10)
        self.task = Task.objects.create(
            name="test",
            platform="Rent591",
            url="https://www.591.com.tw/",
            frequency=frequency
        )
        self.run = Run.objects.create(task=self.task, start_time=timezone.now())

    def test_period_search_tasks(self):
        system_tasks.period_search_tasks()
