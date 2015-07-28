from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import User

#connect to db
engine=create_engine('sqlite:///users.db')

#session factory
Session=sessionmaker(bind=engine)

#session object
session=Session()

#read data from db
rows=session.query(User)

#print it
for row in rows:
	print row






