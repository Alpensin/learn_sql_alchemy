from datetime import datetime

from sqlalchemy import Index, Integer, String, Column, DateTime, PrimaryKeyConstraint, \
    UniqueConstraint, ForeignKeyConstraint
from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer)
    username = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(200), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('id', name='user_pk'),
        UniqueConstraint('username'),
        UniqueConstraint('email'),
    )


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    slug = Column(String(100), nullable=False)
    content = Column(String(50), nullable=False)
    published = Column(String(200), nullable=False, default=False)
    user_id = Column(Integer(), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['users.id']),
        Index('title_content_index' 'title', 'content'),
    )

    def __repr__(self):
        return f'Post({self.id=}, {self.title=}, {self.slug=})'


engine = create_engine("postgresql+psycopg2://postgres:123@localhost/test_db", echo=True)

Session = sessionmaker(bind=engine)
session = Session()
# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)

print(session)
db_data = inspect(engine)
print('created tables', db_data.get_table_names())
print(session.query(Post).all())
session.close()