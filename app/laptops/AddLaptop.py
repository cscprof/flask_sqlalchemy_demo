# Import the database object
from app.extensions import Base, engine, session
from sqlalchemy import insert

# Import thr models that we need
from app.models.processor import Processor
from app.models.laptop import Laptop


class AddLaptop:

    '''
    Accept form data for a new laptop and add it to the database
    '''
    def laptop_add(self, form):        
        
        # Create an instance of the Laptop model
        session.execute(
            insert(Laptop),
            [
                {
                    "brand": form.brand.data,
                    "model": form.model.data,
                    "price": form.price.data,
                    "rating": form.rating.data,
                    "ram_memory": form.ram_memory.data,
                    "touch_screen": int(form.touch_screen.data),
                    "processor_id": form.processor_id.data
                }
            ]
        )

        # Commit the insert to the database and return the ID of the inserted record
        session.commit()
        return Laptop.id


    '''
    Create a list of processors to be used in the laptop dropdown list
    '''
    def buildProcessorList(self):

        # Get all processors
        Base.metadata.create_all(engine)

        results = session.query(Processor).all()

        # Create list of tuples (id, processor type)
        choices = [(-1, "-- Select --")]
        for item in results:
            processor_name = item.processor_brand + " " + item.processor_name
            choices.append( (item.processor_id, processor_name) )

        return choices