from pydantic import BaseModel
from typing import Optional


class BaseFilter(BaseModel):
    def dict(self):
        filter_kwargs = super().dict()
        return {
            key: value
            for key, value in filter_kwargs.items()
            if value not in [None, ""]
        }
