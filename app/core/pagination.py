from pydantic import BaseModel
from typing import Optional


class LimitOffsetPagination(BaseModel):
    limit: int
    offset: Optional[int]

    def response_pagination(self, queryset, total):
        return {"total": total, "data": list(queryset)}


class PaginationSchema(BaseModel):
    total: int
