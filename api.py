import requests
import json

import database

data = database.Database()

class Api:
    """
    Here we will create an Api class which will make the calls 
    to the API of Openfoodfact to retrieve the information 
    and store it in our database.
    """

    def __init__(self):
        self.off = requests.get("https://fr.openfoodfacts.org")
        self.status = self.off.status_code

    # Writing to the database of Category
    def list_category(self):
        data.cursor.execute("INSERT IGNORE INTO Category (category) VALUES (\"Mueslis\")")
        data.cursor.execute("INSERT IGNORE INTO Category (category) VALUES (\"Mayonnaises\")")
        data.cursor.execute("INSERT IGNORE INTO Category (category) VALUES (\"Soupes\")")
        data.cursor.execute("INSERT IGNORE INTO Category (category) VALUES (\"Chips\")")
        data.db.commit()

    # Openfoodfact API call to retrieve data from the best muesli
    def choice_1_A(self):
        liste = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=mueslis&tagtype_1=nutrition_grades&tag_contains_1=contains&additives=without&ingredients_from_palm_oil=without&json=true")
        json_liste = liste.json()
        product_liste = json_liste['products'][0]['product_name']
        product_liste_url = json_liste['products'][0]['url']
        product_liste_id = json_liste['products'][0]['_id']
        product_liste_store = json_liste['products'][0]['stores']
        product_liste_ingredients = json_liste['products'][0]['ingredients_text_fr']
        product_liste_grade = json_liste['products'][0]['nutrition_grade_fr']
        data.cursor.execute("INSERT IGNORE INTO Products_Mueslis_A (product_name, store, ingredients, grade, url, product_id) VALUES (\"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\")".format(product_liste, product_liste_store, product_liste_ingredients, product_liste_grade, product_liste_url, product_liste_id))

        data.db.commit()

    # Openfoodfact API call to retrieve data from the worst muesli
    def choice_1_E(self):
        liste = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=mueslis&json=true")
        json_liste = liste.json()
        product_liste = json_liste['products'][0]['product_name']
        product_liste_url = json_liste['products'][0]['url']
        product_liste_id = json_liste['products'][0]['_id']
        product_liste_store = json_liste['products'][0]['stores']
        product_liste_ingredients = json_liste['products'][0]['ingredients_text_fr']
        product_liste_grade = json_liste['products'][0]['nutrition_grade_fr']
        data.cursor.execute("INSERT IGNORE INTO Products_Mueslis_E (product_name, store, ingredients, grade, url, product_id) VALUES (\"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\")".format(product_liste, product_liste_store, product_liste_ingredients, product_liste_grade, product_liste_url, product_liste_id))

        data.db.commit()
        x=0
        while x < 11:
            product_liste = json_liste['products'][1+x]['product_name']
            product_liste_url = json_liste['products'][1+x]['url']
            product_liste_id = json_liste['products'][1+x]['_id']
            product_liste_store = json_liste['products'][1+x]['stores']
            product_liste_ingredients = json_liste['products'][1+x]['ingredients_text_fr']
            product_liste_grade = json_liste['products'][1+x]['nutrition_grade_fr']
            data.cursor.execute("INSERT IGNORE INTO Products_Mueslis_E (product_name, store, ingredients, grade, url, product_id) VALUES (\"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\")".format(product_liste, product_liste_store, product_liste_ingredients, product_liste_grade, product_liste_url, product_liste_id))

            data.db.commit()
            x = x+1
    
    # Openfoodfact API call to retrieve data from the best mayonnaises
    def choice_2_A(self):
        liste = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=mayonnaises&tagtype_1=nutrition_grades&tag_contains_1=contains&additives=without&ingredients_from_palm_oil=without&json=true")
        json_liste = liste.json()
        product_liste = json_liste['products'][0]['product_name']
        product_liste_url = json_liste['products'][0]['url']
        product_liste_id = json_liste['products'][0]['_id']
        product_liste_store = json_liste['products'][0]['stores']
        product_liste_ingredients = json_liste['products'][0]['ingredients_text_fr']
        product_liste_grade = json_liste['products'][0]['nutrition_grade_fr']
        data.cursor.execute("INSERT IGNORE INTO Products_Mayonnaises_A (product_name, store, ingredients, grade, url, product_id) VALUES (\"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\")".format(product_liste, product_liste_store, product_liste_ingredients, product_liste_grade, product_liste_url, product_liste_id))

        data.db.commit()

    # Openfoodfact API call to retrieve data from the worst mayonnaises
    def choice_2_E(self):
        liste = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=mayonnaises&json=true")
        json_liste = liste.json()
        product_liste = json_liste['products'][0]['product_name']
        product_liste_url = json_liste['products'][0]['url']
        product_liste_id = json_liste['products'][0]['_id']
        product_liste_store = json_liste['products'][0]['stores']
        product_liste_ingredients = json_liste['products'][0]['ingredients_text_fr']
        product_liste_grade = json_liste['products'][0]['nutrition_grade_fr']
        data.cursor.execute("INSERT IGNORE INTO Products_Mayonnaises_E (product_name, store, ingredients, grade, url, product_id) VALUES (\"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\")".format(product_liste, product_liste_store, product_liste_ingredients, product_liste_grade, product_liste_url, product_liste_id))

        data.db.commit()
        x=0
        while x < 11:
            product_liste = json_liste['products'][1+x]['product_name']
            product_liste_url = json_liste['products'][1+x]['url']
            product_liste_id = json_liste['products'][1+x]['_id']
            product_liste_store = json_liste['products'][1+x]['stores']
            product_liste_ingredients = json_liste['products'][1+x]['ingredients_text_fr']
            product_liste_grade = json_liste['products'][1+x]['nutrition_grade_fr']
            data.cursor.execute("INSERT IGNORE INTO Products_Mayonnaises_E (product_name, store, ingredients, grade, url, product_id) VALUES (\"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\")".format(product_liste, product_liste_store, product_liste_ingredients, product_liste_grade, product_liste_url, product_liste_id))

            data.db.commit()
            x = x+1

    # Openfoodfact API call to retrieve data from the best soupes
    def choice_3_A(self):
        liste = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=soupes&tagtype_1=nutrition_grades&tag_contains_1=contains&additives=without&ingredients_from_palm_oil=without&json=true")
        json_liste = liste.json()
        product_liste = json_liste['products'][0]['product_name']
        product_liste_url = json_liste['products'][0]['url']
        product_liste_id = json_liste['products'][0]['_id']
        product_liste_store = json_liste['products'][0]['stores']
        product_liste_ingredients = json_liste['products'][0]['ingredients_text_fr']
        product_liste_grade = json_liste['products'][0]['nutrition_grade_fr']
        data.cursor.execute("INSERT IGNORE INTO Products_Soupes_A (product_name, store, ingredients, grade, url, product_id) VALUES (\"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\")".format(product_liste, product_liste_store, product_liste_ingredients, product_liste_grade, product_liste_url, product_liste_id))

        data.db.commit()

    # Openfoodfact API call to retrieve data from the worst soupes
    def choice_3_E(self):
        liste = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=soupes&json=true")
        json_liste = liste.json()
        product_liste = json_liste['products'][0]['product_name']
        product_liste_url = json_liste['products'][0]['url']
        product_liste_id = json_liste['products'][0]['_id']
        product_liste_store = json_liste['products'][0]['stores']
        product_liste_ingredients = json_liste['products'][0]['ingredients_text_fr']
        product_liste_grade = json_liste['products'][0]['nutrition_grade_fr']
        data.cursor.execute("INSERT IGNORE INTO Products_Soupes_E (product_name, store, ingredients, grade, url, product_id) VALUES (\"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\")".format(product_liste, product_liste_store, product_liste_ingredients, product_liste_grade, product_liste_url, product_liste_id))

        data.db.commit()
        x=0
        while x < 11:
            product_liste = json_liste['products'][1+x]['product_name']
            product_liste_url = json_liste['products'][1+x]['url']
            product_liste_id = json_liste['products'][1+x]['_id']
            product_liste_store = json_liste['products'][1+x]['stores']
            product_liste_ingredients = json_liste['products'][1+x]['ingredients_text_fr']
            product_liste_grade = json_liste['products'][1+x]['nutrition_grade_fr']
            data.cursor.execute("INSERT IGNORE INTO Products_Soupes_E (product_name, store, ingredients, grade, url, product_id) VALUES (\"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\")".format(product_liste, product_liste_store, product_liste_ingredients, product_liste_grade, product_liste_url, product_liste_id))

            data.db.commit()
            x = x+1

    # Openfoodfact API call to retrieve data from the best chips
    def choice_4_A(self):
        liste = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=chips&tagtype_1=nutrition_grades&tag_contains_1=contains&additives=without&ingredients_from_palm_oil=without&json=true")
        json_liste = liste.json()
        product_liste = json_liste['products'][0]['product_name']
        product_liste_url = json_liste['products'][0]['url']
        product_liste_id = json_liste['products'][0]['_id']
        product_liste_store = json_liste['products'][0]['stores']
        product_liste_ingredients = json_liste['products'][0]['ingredients_text_fr']
        product_liste_grade = json_liste['products'][0]['nutrition_grade_fr']
        data.cursor.execute("INSERT IGNORE INTO Products_Chips_A (product_name, store, ingredients, grade, url, product_id) VALUES (\"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\")".format(product_liste, product_liste_store, product_liste_ingredients, product_liste_grade, product_liste_url, product_liste_id))

        data.db.commit()

    # Openfoodfact API call to retrieve data from the worst chips
    def choice_4_E(self):
        liste = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=chips&json=true")
        json_liste = liste.json()
        product_liste = json_liste['products'][0]['product_name']
        product_liste_url = json_liste['products'][0]['url']
        product_liste_id = json_liste['products'][0]['_id']
        product_liste_store = json_liste['products'][0]['stores']
        product_liste_ingredients = json_liste['products'][0]['ingredients_text_fr']
        product_liste_grade = json_liste['products'][0]['nutrition_grade_fr']
        data.cursor.execute("INSERT IGNORE INTO Products_Chips_E (product_name, store, ingredients, grade, url, product_id) VALUES (\"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\")".format(product_liste, product_liste_store, product_liste_ingredients, product_liste_grade, product_liste_url, product_liste_id))

        data.db.commit()
        x=0
        while x < 11:
            product_liste = json_liste['products'][1+x]['product_name']
            product_liste_url = json_liste['products'][1+x]['url']
            product_liste_id = json_liste['products'][1+x]['_id']
            product_liste_store = json_liste['products'][1+x]['stores']
            product_liste_ingredients = json_liste['products'][1+x]['ingredients_text_fr']
            product_liste_grade = json_liste['products'][1+x]['nutrition_grade_fr']
            data.cursor.execute("INSERT IGNORE INTO Products_Chips_E (product_name, store, ingredients, grade, url, product_id) VALUES (\"{}\", \"{}\", \"{}\", \"{}\", \"{}\", \"{}\")".format(product_liste, product_liste_store, product_liste_ingredients, product_liste_grade, product_liste_url, product_liste_id))

            data.db.commit()
            x = x+1