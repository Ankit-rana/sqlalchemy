from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,Column,Integer,String

#object of declarative_base class so that class can be connected to Base hierarchy
Base = declarative_base()


#make a new class which will be mapped to table in db
class User(Base):
	__tablename__= 'users'
	id = Column(Integer,primary_key=True)
	name = Column(String)
	password = Column(String)
	def __repr__(self):
		return "name:'%s'"%(self.name)


#connect to a database
engine=create_engine('sqlite:///users.db',echo=True)


#now make class into the table in db
Base.metadata.create_all(engine)


