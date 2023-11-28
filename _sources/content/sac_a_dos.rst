Problème du sac à dos
=====================

Dans un jeu vidéo, le héros dispose d’un sac à dos lui permettant de porter les objets collectés au cours de sa quête. Le sac à dos à une capacité maximale de 10 kg. Le héros doit maximiser la valeur en pièces
d’or des objets contenus dans son sac à dos. On donne pour chaque objet collecté par le héros sa masse en kg et sa valeur en pièces d’or.

-  une cape d'invisibilité valant 15 pièces d'or et pesant 1 kg;
-  une horloge valant 16 pièces d'or et pesant 4 kg;
-  un miroir valant 12 pièces d'or et pesant 4 kg;
-  un antidote valant 8 pièces d'or et pesant 1 kg;
-  une baguette magique valant 10 pièces d'or et pesant 1 kg;
-  un diadème valant 30 pièces d'or et pesant 4 kg;
-  une épée valant 10 pièces d'or et pesant 6 kg.

#. Afin de remplir le sac, on pourrait tester toutes les possibilités et choisir la meilleure d’entre elles. Expliquer comment cet algorithme, qualifié de naïf, permettrait de trouver la ou les solution(s) optimale(s).

#. En observant que le choix de chaque objet est binaire (choisi ou non), combien de possibilités différentes pourrait-on dénombrer avec 7 objets possibles ? Et avec 100 objets ? Conclure sur la durée d’exécution d’un tel algorithme naïf.

#. Un algorithme glouton pourrait également être utilisé. Préciser la différence majeure entre l’algorithme naïf et l’algorithme glouton.

#. À choisir entre la baguette magique et la cape d’invisibilité, quel choix conseillerez-vous à votre héros et pourquoi ?

#. On applique un algorithme glouton en utilisant la masse des objets.

   a. Quelle est la composition du sac ?
   b. Calculer la valeur en pièces d'or du contenu du sac. 

#. On applique un algorithme glouton en ne considérant que la valeur des objets sans dépasser la masse maximale du sac.

   a. Quelle est la composition du sac dans ce cas?
   b. Quelle est la valeur obtenue en pièces d'or?

#. On peut appliquer l'algorithme glouton en utilisant la valeur massique de chaque objet.

   a. Calculer la valeur massique de chaque objet en pièces d’or par kilogramme.
   b. Quel pourrait être le meilleur choix possible à chaque étape d’ajout d’un objet dans le sac ?
   c. Quel pré-traitement faudrait-il effectuer avant de remplir le sac à dos ? Quels objets seraient alors choisis, et dans quel ordre ?
   d. Déterminer la composition du sac à dos en indiquant les objets choisis, leur ordre de choix ainsi que la valeur en pièces d’or et la masse en kilogramme du sac à dos.

#. Écrire, en Python ou en pseudo-code, un algorithme glouton répondant au problème posé. On définira chaque objet par un dictionnaire que l'on rassemblera dans un tableau.

   .. code-block:: Python

      # on construit un dictionnaire pour chaque objet contenant son nom, sa valeur en pièces d'or et sa masse
      # tous les objets sont réunis dans une même liste objets
      cape = {"nom":'cape',"masse":2,"valeur":15}
      horloge = {"nom":'horloge',"masse":4,"valeur":16}
      miroir = {"nom":'miroir',"masse":4,"valeur":12}
      baguette = {"nom":'baguette magique',"masse":1,"valeur":10}
      antidote = {'nom':"antidote","masse":1,"valeur":8}
      epee = {"nom":'épée',"masse":6,"valeur":10}
      diademe = {"nom":"diadème","masse":4,"valeur":30}

      # Tableau contenant les différents objets collectés par le héros
      objets = [cape, horloge, miroir, baguette, antidote, epee, diademe]

#. Comparer les différentes solutions avec la solution optimale. Que peut-on en conclure ?
