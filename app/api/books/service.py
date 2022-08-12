from app.api.books.models import Book
from app.api.books.schema import BookSchemaRequest
from app.core.database import SessionLocal


class BookService:
    session = SessionLocal()
    model = Book

    def create(self, data: BookSchemaRequest):
        book = self.model(**data.dict())
        self.session.add(book)
        self.session.commit()
        return book

    def list(self, limit, offset):
        return list(self.session.query(self.model).limit(limit).offset(offset))

    def get(self, id):
        return self.session.query(self.model).filter_by(id=id).first()

    def update(self, id, data: BookSchemaRequest):
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
