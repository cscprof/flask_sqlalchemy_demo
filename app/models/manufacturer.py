from app.extensions import db
from sqlalchemy import String, Integer, DECIMAL, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class Manufacturer(db.Model):

    # Set this to the name of the table in the database if 
    # different from the class name defined above.
    __tablename__ = "manufacturers"

    # Schema definition
    manufacturerID : Mapped[int] = mapped_column(primary_key=True)    
    manufacturer_name : Mapped[str] = mapped_column(String(50))
    
    
    def __repr__(self):
        return f'<Manufacturer ID: {self.manufacturerID} - {self.manufacturer_name}>'
    

'''

CREATE TABLE `manufacturers` (
  `manufacturerID` int NOT NULL AUTO_INCREMENT,
  `manufacturer_name` varchar(50) NOT NULL,
  PRIMARY KEY (`manufacturerID`),
  UNIQUE KEY `manufacturer_name` (`manufacturer_name`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=latin1;

'''