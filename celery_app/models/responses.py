from pydantic import BaseModel
from typing import Optional


class CrawlerResponse(BaseModel):
    result: dict
    break_point: Optional[dict]
