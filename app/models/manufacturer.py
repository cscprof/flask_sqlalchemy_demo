from app.extensions import Base

from sqlalchemy import Column, Integer, String


class Manufacturer(Base):

    # Set this to the name of the table in the database if 
    # different from the class name defined above.
    __tablename__ = "manufacturers"

    # Schema definition
    manufacturerID = Column(Integer, primary_key=True)    
    manufacturer_name = Column(String(50))
    
    
    def __repr__(self):
        return f'{self.manufacturer_name}>'
    

'''

CREATE TABLE `manufacturers` (
  `manufacturerID` int NOT NULL AUTO_INCREMENT,
  `manufacturer_name` varchar(50) NOT NULL,
  PRIMARY KEY (`manufacturerID`),
  UNIQUE KEY `manufacturer_name` (`manufacturer_name`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=latin1;

'''