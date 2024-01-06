import importlib
from afd.celery import app
from celery_app import INSTALLED_CRAWLERS


def delete_celery_task_by_id(celery_id: str):
    app.control.revoke(celery_id, terminate=True, signal='SIGKILL')


def get_crawler_by_platform(platform: str):
    if INSTALLED_CRAWLERS.get(platform):
        module_path = INSTALLED_CRAWLERS.get(platform).get("module_path")
        module_path, module_class = module_path.rsplit(".", 1)

        return getattr(importlib.import_module(module_path), module_class)

    else:
        raise ValueError(f"暫不支援 {platform} 爬蟲，請重新確認")
