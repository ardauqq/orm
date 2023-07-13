import sqlalchemy
from sqlalchemy.orm import sessionmaker
from orm_models import Publisher, Book, Shop, Stock, Sale, create_tables
from orm_insert import insert_data

DSN = ""
engine = sqlalchemy.create_engine(DSN)

if __name__ == '__main__':
    create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    insert_data()


def get_info(pub_name=input('Name: ')):
    publisher = session.query(Publisher).filter_by(name=pub_name).first()
    query = session.query(Sale).join(Stock).join(Book).join(Publisher).join(Shop)\
        .filter(Publisher.id == publisher.id).all()
    for q in query:
        print(f'{q.stock.book.title} | {q.stock.shop.name} | {q.price} | {q.date_sale}')


if __name__ == '__main__':
    get_info()


session.close()