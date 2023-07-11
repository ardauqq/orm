import sqlalchemy as sq
import datetime as dt
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publisher'

    publisher_id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=30), nullable=False)


class Book(Base):
    __tablename__ = 'book'

    book_id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.Text, nullable=False)
    publisher_id = sq.Column(sq.Integer, sq.ForeignKey('publisher.publisher_id', ondelete='CASCADE'))

    author = relationship('Publisher', backref='book')
    book_count = relationship('Stock', backref='stock')


class Shop(Base):
    __tablename__ = 'shop'

    shop_id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), nullable=False)

    shop_stock = relationship('Stock', backref='stock')


class Stock(Base):
    __tablename__ = 'stock'

    stock_id = sq.Column(sq.Integer, primary_key=True)
    book_id = sq.Column(sq.Integer, sq.ForeignKey('book.book_id'), ondelete='CASCADE')
    shop_id = sq.Column(sq.Integer, sq.ForeignKey('shop.shop_id'), ondelete='CASCADE')
    count = sq.Column(sq.Integer, nullable=False)


class Sale(Base):
    __tablename__ = 'sale'

    sale_id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Numeric, nullable=False)
    stock_id = sq.Column(sq.Integer, sq.ForeignKey('stock.stock_id', ondelete='CASCADE'))
    date_sale = sq.Column(sq.Date, default=dt.date.today)
    count = sq.Column(sq.Integer, nullable=False)

    sale_stock = relationship('Stock', back_populates='stock_sale')


def create_tables(engine):
    #Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
