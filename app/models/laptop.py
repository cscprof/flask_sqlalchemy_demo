from app.extensions import Base

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DECIMAL
from sqlalchemy.orm import relationship

from app.models.processor import Processor

class Laptop(Base):

  # Set this to the name of the table in the database if 
  # different from the class name defined above.
  __tablename__ = "laptops"

  # Schema definition
  id = Column(primary_key=True)
  brand = Column(String(50))
  model = Column(String(255))
  price = Column(DECIMAL)
  rating = Column(Integer)
  ram_memory = Column(Integer)
  touch_screen =Column(Boolean)

  # NOTE: processor will be the variable that refers to processor table columns
  processor_id = Column(Integer, ForeignKey('processors.processor_id'))
  processor = relationship("Processor")  
      
  
  def __repr__(self):
      return f'<Brand "{self.brand} Model: {self.model}">'


'''

CREATE TABLE `laptops` (
  `id` int NOT NULL AUTO_INCREMENT,
  `brand` varchar(50) NOT NULL,
  `model` varchar(255) DEFAULT NULL,
  `price` decimal(10,2) NOT NULL,
  `rating` int DEFAULT NULL,
  `processor_id` int NOT NULL,
  `ram_memory` int DEFAULT NULL,
  `touch_screen` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `laptop_proc` (`processor_id`),
  CONSTRAINT `laptop_proc` FOREIGN KEY (`processor_id`) REFERENCES `processors` (`processor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=997 DEFAULT CHARSET=latin1;    

'''