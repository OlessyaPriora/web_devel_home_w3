from tokenize import String

from sqlalchemy import create_engine, Numeric, Boolean, Integer, Column, String, ForeignKey

from sqlalchemy.orm import sessionmaker, declarative_base, relationship

engine = create_engine('sqlite:///:memory:')


Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(Numeric(10, 2)
    in_stock = Column(Boolean)
    category_id = Column(Integer, ForeignKey('categories.id'))


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(255))
    products = relationship("Product", back_populates="category")

Product.category = relationship("Category", back_populates="products")





