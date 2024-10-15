from app.extensions import engine, session, Base

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

class Processor(Base):

    # Set this to the name of the table in the database if 
    # different from the class name defined above.
    __tablename__ = "processors"

    # Schema definition
    processor_id = Column(Integer, primary_key=True)
    processor_name = Column(String(32))
    processor_brand = Column(String(32))

    laptops = relationship("Laptop")
    
    def __repr__(self):
        return f'<Processor ID: {self.processor_id} is {self.processor_name} {self.processor_brand}>'
    

'''

CREATE TABLE `processors` (
  `processor_id` int NOT NULL AUTO_INCREMENT,
  `processor_name` varchar(32) NOT NULL,
  `processor_brand` varchar(32) NOT NULL,
  PRIMARY KEY (`processor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

'''