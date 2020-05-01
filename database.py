import mysql.connector

class Database:
    """
    This class aims to gather all the classes in MySQL for our project, 
    you will find here all the database.
    """
    def __init__(self):
        self.db = mysql.connector.connect(host= "localhost", user= "root", passwd= "6842tera",)
        self.cursor = self.db.cursor(buffered=True)
        self.commit = self.db.commit()
        self.create_bdd = self.cursor.execute('CREATE DATABASE IF NOT EXISTS Purbeurre')
        self.use = self.cursor.execute('USE Purbeurre')

    # Create table Category
    def create_table_category(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Category ( id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, category VARCHAR(50) NOT NULL UNIQUE, PRIMARY KEY(id)) ENGINE = InnoDB')

    # Create tables for Mueslis
    def create_table_products_mueslis_E(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Products_Mueslis_E (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, product_name VARCHAR(120) NOT NULL, store TEXT, ingredients TEXT, grade TEXT, url TEXT, product_id BIGINT UNSIGNED NOT NULL UNIQUE, PRIMARY KEY(id)) ENGINE = InnoDB')

    def create_table_products_mueslis_A(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Products_Mueslis_A (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, product_name VARCHAR(120) NOT NULL, store TEXT, ingredients TEXT, grade TEXT, url TEXT, product_id BIGINT UNSIGNED NOT NULL UNIQUE, PRIMARY KEY(id)) ENGINE = InnoDB')
        
    # Create tables for Mayonnaises
    def create_table_products_mayonnaises_E(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Products_Mayonnaises_E (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, product_name VARCHAR(120) NOT NULL, store TEXT, ingredients TEXT, grade TEXT, url TEXT, product_id BIGINT UNSIGNED NOT NULL UNIQUE, PRIMARY KEY(id)) ENGINE = InnoDB')
        
    def create_table_products_mayonnaises_A(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Products_Mayonnaises_A (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, product_name VARCHAR(120) NOT NULL, store TEXT, ingredients TEXT, grade TEXT, url TEXT, product_id BIGINT UNSIGNED NOT NULL UNIQUE, PRIMARY KEY(id)) ENGINE = InnoDB')
        
    # Create tables for Soupes
    def create_table_products_soupes_E(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Products_Soupes_E (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, product_name VARCHAR(120) NOT NULL, store TEXT, ingredients TEXT, grade TEXT, url TEXT, product_id BIGINT UNSIGNED NOT NULL UNIQUE, PRIMARY KEY(id)) ENGINE = InnoDB')
        
    def create_table_products_soupes_A(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Products_Soupes_A (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, product_name VARCHAR(120) NOT NULL, store TEXT, ingredients TEXT, grade TEXT, url TEXT, product_id BIGINT UNSIGNED NOT NULL UNIQUE, PRIMARY KEY(id)) ENGINE = InnoDB')
        
    # Create tables for Chips
    def create_table_products_chips_E(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Products_Chips_E (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, product_name VARCHAR(120) NOT NULL, store TEXT, ingredients TEXT, grade TEXT, url TEXT, product_id BIGINT UNSIGNED NOT NULL UNIQUE, PRIMARY KEY(id)) ENGINE = InnoDB')
        
    def create_table_products_chips_A(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Products_Chips_A (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, product_name VARCHAR(120) NOT NULL, store TEXT, ingredients TEXT, grade TEXT, url TEXT, product_id BIGINT UNSIGNED NOT NULL UNIQUE, PRIMARY KEY(id)) ENGINE = InnoDB')
        
    # Tables for Favorite
    def create_table_favorite(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Favorite (id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT, product_name VARCHAR(120) NOT NULL, store TEXT, ingredients TEXT, grade TEXT, url TEXT, product_id BIGINT UNSIGNED NOT NULL UNIQUE, PRIMARY KEY(id)) ENGINE = InnoDB')
