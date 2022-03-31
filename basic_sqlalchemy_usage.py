from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from models import Post, User


engine = create_engine('postgresql+psycopg2://postgres:123@localhost/test_db',
                       echo=True)

Session = sessionmaker(bind=engine)
session = Session()

# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)

print(session)
db_data = inspect(engine)
print('created tables', db_data.get_table_names())
print(session.query(Post).all())
print(session.query(User).all())

session.close()
