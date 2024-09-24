# from .. import mysql

class LaptopListing:

    # Define Queries for the class

    LAPTOP_LIST_QUERY = '''
    SELECT
       id
       , brand
       , model
       , price
       , rating
       , ram_memory
       , touch_screen
       , processor_name
       , processor_brand
    FROM
        laptops l
        inner join processors p  on l.processor_id = p.processor_id
    ORDER BY
        price DESC;
    '''

    # def get_data(self):
    #     cur = mysql.connection.cursor()
    #     cur.execute(self.LAPTOP_LIST_QUERY)
    #     output = cur.fetchall()
    #     return output