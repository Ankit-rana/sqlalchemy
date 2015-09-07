from sqlalchemy import create_engine,Table,Integer,String,Table,Column,MetaData

#lazy connection
engine = create_engine('sqlite:///users.db')

#create metdata and create all tables in it
meta=MetaData()

users = Table('users',meta,
	Column('uid',Integer,primary_key=True),
	Column('name',String(150))
	)
	
#metadata.create_all(engine)
# OR 
#bind the connection to metadata and create
meta.bind=engine
users.create()
