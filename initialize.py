from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from database_setup import Base, Person, Event
from datetime import datetime

engine = create_engine('sqlite:///crudlab.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# You can add some starter data for your database here.

antonio = Person(name = 'Antonio Delegrassi',
				username = 'sexyantonio668',
				password = 'mynameisantonio',
				gender = 'identifies as a chair',
				nationality = 'Spanish',
				bio = 'I identify as a chair because why not',
				rating = 4.5)


pizza_event = Event(title = 'Awesome Pizza Party',
    				date = datetime(2016, 8, 10),
    				chef = 1,
    				description = 'Come learn how to make good pizza! Antonio will be there!')


session.add(antonio)
session.add(pizza_event)
session.commit()