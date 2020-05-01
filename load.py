import api
import database

api = api.Api()
data = database.Database()

class Load:
    """
    This class will execute the creation of the database in order, 
    then the API calls and the writing to the database.
    """

    def __init__(self):
        data.cursor.execute('CREATE DATABASE IF NOT EXISTS Purbeurre')
        data.cursor.execute('USE Purbeurre')
        data.create_table_category()
        data.create_table_products_mueslis_A()
        data.create_table_products_mueslis_E()
        data.create_table_products_mayonnaises_A()
        data.create_table_products_mayonnaises_E()
        data.create_table_products_soupes_A()
        data.create_table_products_soupes_E()
        data.create_table_products_chips_A()
        data.create_table_products_chips_E()
        data.create_table_favorite()
        api.list_category()
        api.choice_1_A()
        api.choice_1_E()
        api.choice_2_A()
        api.choice_2_E()
        api.choice_3_A()
        api.choice_3_E()
        api.choice_4_A()
        api.choice_4_E()
        
        
        
        

if __name__ == "__main__":
    #load = Load()
    data.cursor.execute("DROP DATABASE Purbeurre")
    