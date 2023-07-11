import sqlalchemy
from sqlalchemy.orm import sessionmaker
from orm_models import Publisher, Book, Shop, Stock, Sale, create_tables


DSN = ''
engine = sqlalchemy.create_engine(DSN)


if __name__ == '__main__':
    create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

publisher_name = input('Имя: ')
publisher_id = input('ID: ')


def get_info_by_publisher(p_name=None, p_id=None):
    if p_name is None and p_id is not None:
        for i in session.query(Shop.name).join(Stock.shop_stock).join(Stock.book_count).join(Publisher.author).filter(Publisher.id == int(p_id)):
            yield i
    elif p_name is not None and p_id is None:
        for i in session.query(Shop.name).join(Stock.shop_stock).join(Stock.book_count).join(Publisher.author).filter(Publisher.name == p_name.name):
            yield i
    elif p_name is not None and p_id is not None:
        for i in session.query(Shop.name).join(Stock.shop).join(Stock.book).join(Book.publisher).filter(Publisher.name == p_name, Publisher.id == int(p_id)):
            yield i


session.close()