import abc
from pathlib import Path
from requests import Session
from fake_useragent import UserAgent
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class BaseRequestHandler(abc.ABC):
    headers: dict = {}
    cookies: dict = {}

    def __init__(self, headers: dict = None, cookies: dict = None):
        self.headers.update(headers) if headers else None
        self.cookies.update(cookies) if cookies else None

        cache_path = Path(__file__).parent.parent / "extensions" / "fake_useragent.json"
        user_agent = UserAgent(use_external_data=False, cache_path=str(cache_path))
        self.headers.update({"user-agent": user_agent.google})

    @abc.abstractmethod
    def set_connection(self):
        raise NotImplementedError("必須實作 set_connection 方法")

    @staticmethod
    @abc.abstractmethod
    def close_connection(connection):
        raise NotImplementedError("必須實作 close_connection 方法")

    @abc.abstractmethod
    def request(self, url: str, connection):
        raise NotImplementedError("必須實作 request 方法")


class StaticRequestHandler(BaseRequestHandler):

    def set_connection(self) -> Session:
        session = Session()
        session.headers.update(self.headers) if self.headers else None
        session.cookies.update(self.cookies) if self.cookies else None

        return session

    @staticmethod
    def close_connection(connection: Session):
        connection.close()

    def request(self, url: str, connection: Session) -> str:
        resp = connection.get(url=url)

        return resp.text


class DynamicRequestHandler(BaseRequestHandler):

    def set_connection(self) -> Chrome:
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--headless=chrome")
        options.add_argument("--disable-logging")
        options.add_argument("--window-size=1920,1080")
        options.add_argument(f"user-agent={self.headers.get('user-agent')}")

        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)

        service = Service()
        driver = Chrome(service=service, options=options)

        return driver

    @staticmethod
    def close_connection(connection: Chrome):
        connection.quit()

    def request(self, url: str, connection: Chrome) -> str:
        connection.get(url=url)

        if self.cookies:
            for key, value in self.cookies.items():
                connection.add_cookie({"name": key, "value": value})
            connection.get(url=url)

        return connection.page_source
