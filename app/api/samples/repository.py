from .models import Sample
from app.core.repository import BaseRepository


class SampleRepository(BaseRepository):
    model = Sample
