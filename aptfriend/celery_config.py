from aptfriend.settings import env_settings

# refer: https://docs.celeryq.dev/en/stable/userguide/configuration.html

broker_url = env_settings.REDIS_URL
result_backend = env_settings.REDIS_URL
enable_utc = True
timezone = "Asia/Taipei"
imports = [
    "celery_app.tasks"
]
task_routes = {
    'celery_app.tasks.crawler_task': {
        'queue': 'crawler_queue'
    },
}
