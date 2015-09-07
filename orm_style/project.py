from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import User


print "connecting to db"
engine=create_engine('sqlite:///users.db')

print "session factory"
Session=sessionmaker(bind=engine)

print "session object"
session=Session()

print "read data from db"
rows=session.query(User).all()

print "print it"
for row in rows:
	print row






