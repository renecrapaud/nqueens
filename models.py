import db

from sqlalchemy import Column, Integer, String, Float


class Result(db.Base):
    __tablename__ = 'results'

    id = Column(Integer, primary_key=True)
    result = Column(String, nullable=False)

    def __init__(self, result):
        self.result = result

    def __repr__(self):
        return f'Result({self.result})'

    def __str__(self):
        return self.result