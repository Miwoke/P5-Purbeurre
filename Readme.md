                                    
# P5- PurBeurre


----------


-----------------------------------
Sur ce projet, nous allons utiliser l'API d'OpenFoodFacts, grâce a leur bdd nous allons pouvoir obtenir des substitution d'aliment que l'on souhaiterais remplacer. Les données serons stocker dans une bdd MySQL pour cette occasion, mais une conversion en SQLite et possible en changent dans le script bdd.py.

Une application simple coder en Python sera accessible via un terminal.

#### Bonus :
une interface graphique sera développé en bonus.

------------------------------------------------

## Fonctionnalités :

-----------------------------------------------------
 - Les aliments sont récupérés via l'API de OpenFoodFacts.
 - Le script appel l'API.
 - L' API renvoie les données.
 - Le script insère les données dans une bdd MySQL
 - Un menu affiche deux choix au lancement du programme : 
	 - Sélectionner la catégorie de l'aliment que vous voulez substituer.
		 - L'utilisateur arrive sur un la bdd Catégorie avec une liste de choix précédé d'un chiffre
		 - L'utilisateur et invité a utilisé le paver numérique pour sélectionner sont choix
		 - Une fois le choix réalisé, la bdd correspond au choix s'ouvre et un choix d'aliment lui est proposé
		 - Après le choix d'aliment, une description du produit lui est afficher (Nom du produit et nutrition grade) ainsi qu'un produit de substitution
		 - Il est enfin invité a sauvegardé la recherche dans la bdd Favoris afin d'y avoir accès plus facilement dans l'avenir
	 - Voir les aliments sauvegardés.
		 - L'utilisateur affiche la bdd Favoris qui lui affiche toutes les recherches sauvegardés
		 
---------------------------------------------------------

## Prérequis :

 - Python 3.8 ou supérieur 
 - MySQL SERVER installé
 - Avoir un identifiant MySQL

-------------------------------------

## Installation :

 1. Lancez MySQL.
 2. Pour installer les packages requis, exécutez la commande : `py -m pip install -r requirements.txt`
 
 #### Note : l'installation d'un environnement virtuel n'est pas obligatoire, mais conseiller. 

-----------------------------------

## Mise en route :

 - Exécutez le script avec : `python3 main.py`
 - Le script s'occuperas de crée la bdd si celle-ci n'est pas présente

------------------------

## Exemple d'utilisation

# Menu

 >>> 1. Quel aliment souhaitez-vous remplacer ?

 >>> 2. Voir mes aliments favoris

 >>> 3. Quitter

Entrez votre choix ici entre 1 et 3 :

------------------------

# Choix 1

>> 1 - Mueslis
>> 2 - Mayonnaises
>> 3 - Soupes
>> 4 - Chips


Entrez votre choix ici entre 1 et 4 ou (revenir au menu 5), (aller au favorie 6), (quitter le script 7):

------------------------

# Choix Mayonnaises

>> 1 - Mayonnaise de Dijon
>> 2 - Mayonnaise aux Œufs Frais
>> 3 - Mayonnaise aux oeufs frais
>> 4 - Mayonnaise aux Œufs Frais
>> 5 - Mayonnaise Bénédicta comme à la maison
>> 6 - Mayonnaise
>> 7 - Mayonnaise aux œufs frais
>> 8 - Mayonnaise
>> 9 - La Classique
>> 10 - Amora Mayonnaise de Dijon Nature Œufs de poules élevées en plein air 470g
>> 11 - Amora Mayonnaise Recette Fouettée Flacon Souple 398g
>> 12 - Maille Mayonnaise Fins Gourmets Bocal 320g

Entrez votre choix ici entre 1 et 12 :

------------------------

# Choix 4

>> Nom : Mayonnaise aux Œufs Frais
>> Nutrition Grade : e

Pour ce type de produit, nous vous conseillons celui-ci :

>> Nom : Mayonnaise Bénédicta comme à la maison
>> Nutrition Grade : d

Sauvegarder votre recherche ? 1 pour validé, 2 pour retourner au menu, 0 pour quitter: 1
savegarder dans vos favoris

Voir mes favories ? 1 pour validé, 2 pour retourner au menu, 0 pour quitter :