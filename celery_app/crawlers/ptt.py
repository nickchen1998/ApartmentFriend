from bs4 import BeautifulSoup
from .base import BaseCrawler
from requests.sessions import Session
from models.responses import CrawlerResponse


class PTTCrawler(BaseCrawler):

    def parse(self, page_source: str, connection: Session, **kwargs) -> CrawlerResponse:
        result = CrawlerResponse()
        url = "https://www.ptt.cc/bbs/sex/index.html"

        result.datas["titles"] = []
        result.datas["titles"].extend(self.get_titles(page_source=page_source))

        page_source = self.request_handler.request(url=url, connection=connection)
        result.datas["titles"].extend(self.get_titles(page_source=page_source))

        return result

    @staticmethod
    def get_titles(page_source):
        soup = BeautifulSoup(page_source, "lxml")
        titles = soup.find_all(name="div", attrs={"class": "title"})

        return [title.text.replace("\n", "") for title in titles]
