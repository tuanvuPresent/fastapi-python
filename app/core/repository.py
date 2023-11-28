from app.core.database import SessionLocal


class BaseRepository:
    session = SessionLocal()
    model = None

    def create(self, data: dict):
        instance = self.model(**data.dict())
        self.session.add(instance)
        self.session.commit()
        return instance

    def list(self, filters: dict = {}, pagination=None):
        queryset = self.session.query(self.model).filter_by(**filters)
        if pagination:
            total = queryset.count()
            queryset = queryset.limit(pagination.limit).offset(pagination.offset)
            return pagination.response_pagination(queryset, total)
        return list(queryset)

    def get(self, id):
        return self.session.query(self.model).filter_by(id=id).first()

    def update(self, id, data: dict):
        instance = self.session.query(self.model).filter_by(id=id).first()
        if instance:
            for field, value in data.dict().items():
                setattr(instance, field, value)
            self.session.commit()
        return instance

    def delete(self, id):
        instance = self.session.query(self.model).filter_by(id=id).first()
        if instance:
            self.session.delete(instance)
            self.session.commit()
        return instance
