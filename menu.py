import os 

import load
import api
import database

api=api.Api()
data=database.Database()
load = load.Load()

data.cursor.execute('USE Purbeurre')

class Menu:
    """
    In this class we will execute code which will take care of retrieving 
    the information stored in the various databases for the used and 
    to make the user interact
    """

    # Simple menu terminal
    def select_menu(self):
        print('--------------------- MENU ---------------------')
        print()
        print(" >>> 1. Quel aliment souhaitez-vous remplacer ?")
        print()
        print(" >>> 2. Voir mes aliments favoris")
        print()
        print(" >>> 3. Quitter")
        print()
    
    # Here we group the different categories of our food for the used
    def select_category(self):
        print("--------------------- CATEGORIES ---------------------")
        print()
        data.cursor.execute("SELECT category FROM Category ORDER BY id")
        c = data.cursor.fetchall()
        i = 0
        while i < len(c):
            st =' '.join(c[i])
            print(">> {} - ".format(i+1) + st)
            i += 1
        print()
        print()
    
    # Worst mueslis database
    def select_product_muesli_e(self):
        print("--------------------- LISTE PRODUIT ---------------------")
        print()
        data.cursor.execute("SELECT product_name FROM Products_Mueslis_E")
        p = data.cursor.fetchall()
        i = 0
        while i < len(p):
            st =' '.join(p[i])
            print(">> {} - ".format(i+1) + st)
            i += 1
        print()
    
    # Best mueslis database
    def select_product_mueslis_a(self):
        print("--------------------- LISTE PRODUIT ---------------------")
        print()
        data.cursor.execute("SELECT product_name FROM Products_Mueslis_A")
        p = data.cursor.fetchall()
        i = 0
        while i < len(p):
            st =' '.join(p[i])
            print(">> {} - ".format(i+1) + st)
            i += 1
        print()

    # Worst mayonnaises database
    def select_product_mayonnaises_e(self):
        print("--------------------- LISTE PRODUIT ---------------------")
        print()
        data.cursor.execute("SELECT product_name FROM Products_Mayonnaises_E")
        p = data.cursor.fetchall()
        i = 0
        while i < len(p):
            st =' '.join(p[i])
            print(">> {} - ".format(i+1) + st)
            i += 1
        print()

    # Best mayonnaise database
    def select_product_mayonnaises_a(self):
        print("--------------------- LISTE PRODUIT ---------------------")
        print()
        data.cursor.execute("SELECT product_name FROM Products_Mayonnaises_A")
        p = data.cursor.fetchall()
        i = 0
        while i < len(p):
            st =' '.join(p[i])
            print(">> {} - ".format(i+1) + st)
            i += 1
        print()

    # Worst soups database
    def select_product_soupes_e(self):
        print("--------------------- LISTE PRODUIT ---------------------")
        print()
        data.cursor.execute("SELECT product_name FROM Products_Soupes_E")
        p = data.cursor.fetchall()
        i = 0
        while i < len(p):
            st =' '.join(p[i])
            print(">> {} - ".format(i+1) + st)
            i += 1
        print()

    # # Best soups database
    def select_product_soupes_a(self):
        print("--------------------- LISTE PRODUIT ---------------------")
        print()
        data.cursor.execute("SELECT product_name FROM Products_Soupes_A")
        p = data.cursor.fetchall()
        i = 0
        while i < len(p):
            st =' '.join(p[i])
            print(">> {} - ".format(i+1) + st)
            i += 1
        print()

    # Worst crisps database
    def select_product_chips_e(self):
        print("--------------------- LISTE PRODUIT ---------------------")
        print()
        data.cursor.execute("SELECT product_name FROM Products_Chips_E")
        p = data.cursor.fetchall()
        i = 0
        while i < len(p):
            st =' '.join(p[i])
            print(">> {} - ".format(i+1) + st)
            i += 1
        print()

    # Best crisps database
    def select_product_chips_a(self):
        print("--------------------- LISTE PRODUIT ---------------------")
        print()
        data.cursor.execute("SELECT product_name FROM Products_Chips_A")
        p = data.cursor.fetchall()
        i = 0
        while i < len(p):
            st =' '.join(p[i])
            print(">> {} - ".format(i+1) + st)
            i += 1
        print()
    
    # Here we retrieve the information stored in the preferred database for those used
    def select_favorite(self):
        print("--------------------- FAVORIES ---------------------")
        print()
        data.cursor.execute("SELECT product_name, store, ingredients, url, product_id FROM Favorite")
        f = data.cursor.fetchall()
        i = 0
        while i < len(f):
            st =''.join(str(f[i]))
            print(">> {} - ".format(i+1) + st)
            i += 1
        print()
        choice_favorite = int(input("Entrez votre choix ici, (revenir au menu 1), (quitter 2) : "))
        print()
        if choice_favorite == 1:
            self.main_menu()
            
        elif choice_favorite == 2:
            print("Quitter")
            exit()

    # We create a comparator between the worst mueslis and the best
    def choice_products_1(self):

        p_choice = int(input("Entrez votre choix ici entre 1 et 12 : "))
        print()
        print("--------------------- PRODUIT --------------------- ")
        print()
        data.cursor.execute("SELECT product_name, grade FROM Products_Mueslis_E WHERE id={}".format(p_choice))
        f = data.cursor.fetchall()
        i = 0
        while i < len(f):
            st =' \n>> Nutrition Grade : '.join(f[i])
            print(">> Nom : " + st)
            i += 1
        print()
        data.cursor.execute("SELECT product_name, grade FROM Products_Mueslis_A WHERE id=1")
        a = data.cursor.fetchall()
        print("Pour ce type de produit, nous vous conseillons celui-ci : ")
        print()
        i = 0
        while i < len(a):
            st =' \n>> Nutrition Grade : '.join(a[i])
            print(">> Nom : " + st)
            i += 1
        print()
        save = int(input("Sauvegarder votre recherche ? 1 pour validé, 2 pour retourner au menu, 0 pour quitter: "))
        if save == 1:
            data.cursor.execute("INSERT INTO Favorite (product_name, store, ingredients, url, product_id) SELECT product_name, store, ingredients, url, product_id FROM Products_Mueslis_A WHERE id=1")
            data.db.commit()
            print("savegarder dans vos favoris")
            print()
            fav = int(input("Voir mes favories ? 1 pour validé, 2 pour retourner au menu, 0 pour quitter : "))
            if fav == 1:
                self.select_favorite()
            
            elif fav == 2:
                self.main_menu()

            elif fav == 0:
                print("Quitter")
                exit()
            else:
                print("Votre choix et incorrecte")
                self.choice_products_1()

        elif save == 2:
            self.main_menu()
        elif save == 0:
            print("Quitter")
            exit()
        else:
            print("Votre choix et incorrecte")
            self.choice_products_1()

    # We create a comparator between the worst mayonnaises and the best
    def choice_products_2(self):

        p_choice = int(input("Entrez votre choix ici entre 1 et 12 : "))
        print()
        print("--------------------- PRODUIT --------------------- ")
        print()
        data.cursor.execute("SELECT product_name, grade FROM Products_Mayonnaises_E WHERE id={}".format(p_choice))
        f = data.cursor.fetchall()
        i = 0
        while i < len(f):
            st =' \n>> Nutrition Grade : '.join(f[i])
            print(">> Nom : " + st)
            i += 1
        print()
        data.cursor.execute("SELECT product_name, grade FROM Products_Mayonnaises_A WHERE id=1")
        a = data.cursor.fetchall()
        print("Pour ce type de produit, nous vous conseillons celui-ci : ")
        print()
        i = 0
        while i < len(a):
            st =' \n>> Nutrition Grade : '.join(a[i])
            print(">> Nom : " + st)
            i += 1
        print()
        save = int(input("Sauvegarder votre recherche ? 1 pour validé, 2 pour retourner au menu, 0 pour quitter: "))
        if save == 1:
            data.cursor.execute("INSERT INTO Favorite (product_name, store, ingredients, url, product_id) SELECT product_name, store, ingredients, url, product_id FROM Products_Mayonnaises_A WHERE id=1")
            data.db.commit()
            print("savegarder dans vos favoris")
            print()
            fav = int(input("Voir mes favories ? 1 pour validé, 2 pour retourner au menu, 0 pour quitter : "))
            if fav == 1:
                self.select_favorite()
            
            elif fav == 2:
                self.main_menu()

            elif fav == 0:
                print("Quitter")
                exit()
            else:
                print("Votre choix et incorrecte")
                self.choice_products_2()
                
        elif save == 2:
            self.main_menu()
        elif save == 0:
            print("Quitter")
            exit()
        else:
            print("Votre choix et incorrecte")
            self.choice_products_2()

    # We create a comparator between the worst soups and the best
    def choice_products_3(self):

        p_choice = int(input("Entrez votre choix ici entre 1 et 12 : "))
        print()
        print("--------------------- PRODUIT --------------------- ")
        print()
        data.cursor.execute("SELECT product_name, grade FROM Products_Soupes_E WHERE id={}".format(p_choice))
        f = data.cursor.fetchall()
        i = 0
        while i < len(f):
            st =' \n>> Nutrition Grade : '.join(f[i])
            print(">> Nom : " + st)
            i += 1
        print()
        data.cursor.execute("SELECT product_name, grade FROM Products_Soupes_A WHERE id=1")
        a = data.cursor.fetchall()
        print("Pour ce type de produit, nous vous conseillons celui-ci : ")
        print()
        i = 0
        while i < len(a):
            st =' \n>> Nutrition Grade : '.join(a[i])
            print(">> Nom : " + st)
            i += 1
        print()
        save = int(input("Sauvegarder votre recherche ? 1 pour validé, 2 pour retourner au menu, 0 pour quitter: "))
        if save == 1:
            data.cursor.execute("INSERT INTO Favorite (product_name, store, ingredients, url, product_id) SELECT product_name, store, ingredients, url, product_id FROM Products_Soupes_A WHERE id=1")
            data.db.commit()
            print("savegarder dans vos favoris")
            print()
            fav = int(input("Voir mes favories ? 1 pour validé, 2 pour retourner au menu, 0 pour quitter : "))
            if fav == 1:
                self.select_favorite()
            
            elif fav == 2:
                self.main_menu()

            elif fav == 0:
                print("Quitter")
                exit()
            else:
                print("Votre choix et incorrecte")
                self.choice_products_3()
                
        elif save == 2:
            self.main_menu()
        elif save == 0:
            print("Quitter")
            exit()
        else:
            print("Votre choix et incorrecte")
            self.choice_products_3()

    # We create a comparator between the worst crips and the best
    def choice_products_4(self):

        p_choice = int(input("Entrez votre choix ici entre 1 et 12 : "))
        print()
        print("--------------------- PRODUIT --------------------- ")
        print()
        data.cursor.execute("SELECT product_name, grade FROM Products_Chips_E WHERE id={}".format(p_choice))
        f = data.cursor.fetchall()
        i = 0
        while i < len(f):
            st =' \n>> Nutrition Grade : '.join(f[i])
            print(">> Nom : " + st)
            i += 1
        print()
        data.cursor.execute("SELECT product_name, grade FROM Products_Chips_A WHERE id=1")
        a = data.cursor.fetchall()
        print("Pour ce type de produit, nous vous conseillons celui-ci : ")
        print()
        i = 0
        while i < len(a):
            st =' \n>> Nutrition Grade : '.join(a[i])
            print(">> Nom : " + st)
            i += 1
        print()
        save = int(input("Sauvegarder votre recherche ? 1 pour validé, 2 pour retourner au menu, 0 pour quitter: "))
        if save == 1:
            data.cursor.execute("INSERT INTO Favorite (product_name, store, ingredients, url, product_id) SELECT product_name, store, ingredients, url, product_id FROM Products_Chips_A WHERE id=1")
            data.db.commit()
            print("savegarder dans vos favoris")
            print()
            fav = int(input("Voir mes favories ? 1 pour validé, 2 pour retourner au menu, 0 pour quitter : "))
            if fav == 1:
                self.select_favorite()
            
            elif fav == 2:
                self.main_menu()

            elif fav == 0:
                print("Quitter")
                exit()
            else:
                print("Votre choix et incorrecte")
                self.choice_products_4()
                
        elif save == 2:
            self.main_menu()
        elif save == 0:
            print("Quitter")
            exit()
        else:
            print("Votre choix et incorrecte")
            self.choice_products_4()

    # Here we run the code, it's the main menu of the script
    def main_menu(self):
        self.select_menu()
        
        choice_menu = int(input("Entrez votre choix ici entre 1 et 3 : "))
        print()

        # Category
        if choice_menu == 1:
            self.select_category()

            choice_category = int(input("Entrez votre choix ici entre 1 et 4 ou (revenir au menu 5), (aller au favorie 6), (quitter le script 7): "))
            
            if choice_category == 1:
                self.select_product_muesli_e()
                self.choice_products_1()

            elif choice_category == 2:
                self.select_product_mayonnaises_e()
                self.choice_products_2()
            
            elif choice_category == 3:
                self.select_product_soupes_e()
                self.choice_products_3()
            
            elif choice_category == 4:
                self.select_product_chips_e()
                self.choice_products_4()
            
            elif choice_category == 5:
                self.main_menu()
            
            elif choice_category == 6:
                self.select_favorite()
            
            elif choice_category == 7:
                print("Quitter")
                exit()
            
            else:
                print("Ce choix ne correspond pas, veuillez recommencer")
                self.main_menu()

        # Favorite
        elif choice_menu == 2:
            self.select_favorite()
        
        # Quit
        else:
            print("Quitter")
            exit()


if __name__ == "__main__":
    menu=Menu()
    menu.main_menu()