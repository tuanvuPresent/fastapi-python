from .models import Sample
from .repository import SampleRepository
from .schema import SampleSchemaRequest
from app.core.database import SessionLocal


class SampleService:
    repository = SampleRepository()

    def create(self, data: SampleSchemaRequest):
        return self.repository.create(data)

    def list(self, filters: dict = {}, pagination=None):
        return self.repository.list(filters, pagination)

    def get(self, id):
        return self.repository.get(id)

    def update(self, id, data: SampleSchemaRequest):
        return self.repository.update(id=id, data=data)

    def delete(self, id):
        return self.repository.delete(id=id)
