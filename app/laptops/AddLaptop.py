# Import the database object
from app.extensions import db

# Import thr models that we need
from app.models.processor import Processor
from app.models.laptop import Laptop


class AddLaptop:

    '''
    Accept form data for a new laptop and add it to the database
    '''
    def laptop_add(self, form):
        pass
        
        # Create an instance of the Laptop model        
        new_laptop = Laptop(
            brand = form.brand.data,
            model =form.model.data,
            price =form.price.data,
            rating = form.rating.data,
            ram_memory = form.ram_memory.data,
            touch_screen = int(form.touch_screen.data),
            processor_id = form.processor_id.data
        )

        db.session.add(new_laptop)
        db.session.commit()

        return new_laptop.id


    '''
    Create a list of processors to be used in the laptop dropdown list
    '''
    def buildProcessorList(self):

        # Get all processors
        results = Processor.query.all()

        # Create list of tuples (id, processor type)
        choices = [(-1, "-- Select --")]
        for item in results:
            processor_name = item.processor_brand + " " + item.processor_name
            choices.append( (item.processor_id, processor_name) )

        return choices