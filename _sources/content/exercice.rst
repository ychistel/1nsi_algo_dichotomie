Exercices
===========

Exercice 1
----------

Soit ``T`` le tableau trié ``T=[8, 8, 17, 21, 23, 27, 28, 45, 57, 71, 77, 84, 88, 95, 97]``

#. On recherche le nombre ``23`` dans le tableau ``T``. 

   a. Donner les différentes étapes de la recherche par dichotomie dans le tableau pour trouver ce nombre.
   b. Combien d’itérations ont été nécessaires pour touver le nombre cherché ?

#. On cherche le nombre ``75``. Combien d'itérations doit-on prévoir pour vérifier qu'il n'est pas dans le tableau ``T``?

Exercice 2
----------

On redonne l'algorithme de recherche par dichotomie écrit en pseudo-code :

.. code-block:: text

   deb = 0
   fin = indice du dernier élement

   tant que deb <= fin:
      mil = (deb + fin)//2 (m est l'indice de la valeur médiane du tableau t)
      si v < t[mil]:
         fin = mil-1 #(v se trouve dans la première moitié du tableau t)
      
      sinon si v > t[mil]:
         deb = mil + 1  #(v se trouve dans la seconde moitié du tableau)

      sinon: # (on a v = t[mil])
         la valeur est trouvée et a pour indice mil

   on sort de la boucle, la valeur n'est pas trouvée

La fonction ``recherche_dico`` prend en paramètres un tableau ``t`` trié et un nombre ``n``. La fonction renvoie un booléen égal à ``True`` si le nombre ``n`` est dans le tableau et ``False`` dans le cas contraire.

Écrire le code de la fonction ``recherche_dico`` en vous aidant de l'algorithme donné ci-dessus.

Exercice 3
----------

On souhaite mesurer le temps de recherche d'un nombre dans un tableau trié. On donne la fonction ``mesure`` ci-après pour mesurer le temps d'exécution de la recherche par dichotomie d'une valeur.

.. literalinclude:: ../python/mesure.py
   :lines: 1-27

#. Ajouter le code de votre fonction ``recherche_dico`` juste après la ligne d'import et juste avant le code de la fonction ``mesure``.
#. Les mesures sont réalisées sur des tableaux contenant les ``n`` premiers nombres entiers en commençant à 1. Compléter le code dans la fonction mesure pour créer un tableau ``t`` ordonné de nombres.
#. On cherche dans le tableau la valeur 0. Comme elle n'y est pas, c'est la complexité dans le pire des cas. Pour mesurer le temps d'exécution de la fonction sur un tableau de 1000 nombres, il faut saisir en console l'instruction :

   >>> mesure("recherche_dico",1000)

   a. Effectuer des mesures de recherche par dichotomie sur des tableaux de dimensions différentes et compléter le tableau ci-dessous:

      +-------------+------+------+------+------+------+------+-------+
      | dimension n | 1000 | 2000 | 3000 | 4000 | 5000 | 8000 | 10000 |
      +-------------+------+------+------+------+------+------+-------+
      | temps en s  |      |      |      |      |      |      |       |
      +-------------+------+------+------+------+------+------+-------+
   
   b. Le temps de recherche augmente-t-il proportionnellement par rapport à la dimension ``n`` du tableau ?