import abc
from typing import Union
from selenium.webdriver import Chrome
from requests.sessions import Session
from selenium.common.exceptions import InvalidSessionIdException
from celery_app.models.enums import RequestType
from celery_app.models.responses import CrawlerResponse
from celery_app.handler.requests import StaticRequestHandler, DynamicRequestHandler


class BaseCrawler(abc.ABC):
    name: str = ""
    base_url: str = ""
    headers: dict = None
    cookies: dict = None
    request_type: RequestType = RequestType.STATIC
    request_handler: Union[StaticRequestHandler, DynamicRequestHandler]

    def set_request_handler(self):
        if self.request_type is RequestType.STATIC:
            self.request_handler = StaticRequestHandler(headers=self.headers, cookies=self.cookies)
        else:
            self.request_handler = DynamicRequestHandler(headers=self.headers, cookies=self.cookies)

        return self.request_handler.set_connection()

    @abc.abstractmethod
    def parse(self, page_source: str, connection: Union[Chrome, Session], **kwargs) -> CrawlerResponse:
        pass

    def _pares(self, page_source: str, connection: Union[Chrome, Session], **kwargs):
        return self.parse(page_source=page_source, connection=connection, **kwargs)

    def run(self, url: str):
        self.base_url = url
        connection: Union[Chrome, Session] = self.set_request_handler()

        try:
            page_source = self.request_handler.request(url=url, connection=connection)
            result = self._pares(page_source=page_source, connection=connection)
            self.request_handler.close_connection(connection=connection)

            return result

        # selenium docker image 有可能會提前關閉 session 導致任務失敗，這部分無須再做關閉 session 動作
        except InvalidSessionIdException:
            raise

        except Exception:
            self.request_handler.close_connection(connection=connection)
            raise

    def __str__(self):
        return self.name
