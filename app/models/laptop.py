from typing import Optional
from sqlalchemy import String, Integer, DECIMAL, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Import Database connection
from app.extensions import db

class Laptop(db.Model):

  # Set this to the name of the table in the database if 
  # different from the class name defined above.
  __tablename__ = "laptops"

  # Schema definition
  id : Mapped[int] = mapped_column(primary_key=True)
  brand : Mapped[str] = mapped_column(String(50))
  model : Mapped[str] = mapped_column(String(255))
  price : Mapped[DECIMAL] = mapped_column(DECIMAL)
  rating : Mapped[int] = mapped_column(Integer)
  ram_memory : Mapped[int] = mapped_column(Integer)
  touch_screen : Mapped[bool] = mapped_column(Boolean)

  # NOTE: processor will be the variable that refers to processor table columns
  processor_id : Mapped[int] = mapped_column(ForeignKey("processors.processor_id"))
  processor: Mapped["Processor"] = relationship()  
      
  
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