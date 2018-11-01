from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :
def create_product(name,price, quantity,description):
    product = Product(
    	name=name,
        price=price,
        quantity=quantity,
        description=description)
    if product.price>300:
    	print("errorrrrrrrrrrrrrr")
    else:
    	session.add(product)
    	session.commit()

def update_product(name, price,quantity):
   product = session.query(
       Product).filter_by(
       name=name).first()
   if product.price>300:
    	print("errorrrrrrrrrrrrrr")
   else:
   		product.price = price
   product.quantity=quantity
   session.commit()



def delete_product(id):
	session.query(Product).filter_by(id=id).delete()
	session.commit()

def get_product(id):
  pass
