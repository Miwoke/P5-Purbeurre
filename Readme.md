                                    
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
		 - Après le choix d'aliment, une description du produit lui est afficher (ingrédients, un lieu ou l'acheter et un lien url vers la page OpenFoodFacts correspondante).
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
 - Entrez votre nom d'utilisateur MySQL et votre mot de passe.

------------------------
