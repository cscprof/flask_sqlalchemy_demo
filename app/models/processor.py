from app.extensions import db
from sqlalchemy import String, Integer, DECIMAL, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

class Processor(db.Model):

    # Set this to the name of the table in the database if 
    # different from the class name defined above.
    __tablename__ = "processors"

    # Schema definition
    processor_id : Mapped[int] = mapped_column(primary_key=True)
    
    processor_name : Mapped[str] = mapped_column(String(32))
    processor_brand : Mapped[str] = mapped_column(String(32))
    
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