from selenium.webdriver import Chrome
from models.responses import CrawlerResponse
from celery_app.crawlers.base import BaseCrawler


class Rent591(BaseCrawler):
    name: str = "rent591"
    base_url: str = "https://www.591.com.tw/"

    def parse(self, page_source: str, connection: Chrome, **kwargs) -> CrawlerResponse:
        pass
