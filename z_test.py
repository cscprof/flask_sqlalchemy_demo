import os
from flask import Flask
from config import config

# Import the database
from sqlalchemy import create_engine, Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# Launch app and define where the static assets will be located
app = Flask(__name__, static_url_path='/static')

# Get configuration data from settings.conf via the config class
config_name = 'default'
app.config.from_object(config[config_name])
config[config_name].init_app(app)

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

Session = sessionmaker(bind=engine)
session = Session()

# Create the Models
Base = declarative_base()

class FirstLast(Base):
    __tablename__ = 'zfirstlast'
    id = Column(Integer, primary_key = True)
    first_id = Column('first_id', Integer, ForeignKey('zfirstname.id'))
    last_id = Column('last_id', Integer, ForeignKey('zlastname.id'))


class FirstName(Base):
    __tablename__ = 'zfirstname'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(64))
    nickname = Column(String(64))
    lasts = relationship('LastName', secondary='zfirstlast', back_populates='firsts')


class LastName(Base):
    __tablename__ = 'zlastname'

    id= Column(Integer, primary_key=True)
    lastname = Column(String(64))
    firsts = relationship('FirstName', secondary='zfirstlast', back_populates='lasts')





@app.route('/')
def test_page():
   
    Base.metadata.create_all(engine)
    # people = session.query(FirstName).all()
    people = session.query(FirstName).all()
    for person in people:
        # print(person.firstname)
        lnames = [last.lastname for last in person.lasts ]
        print(f"{person.firstname} has these last names: {', '.join(lnames)}")



    return '<h1>Testing the Flask Application Factory Pattern</h1>'



if __name__ == '__main__':
    app.run(debug=True)