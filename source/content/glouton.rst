Algorithme glouton
==================

Certains problèmes ont plusieurs solutions, voire un très grand nombre de solutions. Parmi toutes ces solutions, il en
existe qui sont plus optimales selon les contraintes imposées. La recherche de toutes les solutions peut être
extrêmement gourmand en ressources et en temps d'exécution. Une stratégie, dite glouton, permet d'optimiser le temps de
recherche en proposant une solution qui sera optimale dans certains cas et non optimale dans d'autres cas. Le problème
du rendu de monnaie en est un bon exemple.

Problème du rendu de monnaie
----------------------------

On cherche à égaler une somme à rendre en utilisant le moins d'unités possible prises parmi un sytème défini à l'avance et dont le nombre est illimité. Cela signifie qu'on dispose d'assez d'unités pour rendre une somme quelle qu'elle soit.

Ici on suppose que le système d'unités est le suivant : ``[100, 50, 20, 10, 5, 2, 1]``.

#. Pour rendre la somme de 9 unités, la combinaison qui utlise le moins d'unités est 3 : ``[5, 2, 2]``.

#. Un algorithme dit **glouton** résout ce problème. Cet algorithme enlève la plus grosse unité possible à la somme à rendre jusqu'à ce que la somme à rendre soit nulle.

   En l'appliquant à la somme à rendre de 9 euros :

   -  on enlève la valeur 5 (la plus grande possible) ; il reste à rendre 4 unités
   -  on enlève la valeur 2 ; il reste à rendre 2 unités
   -  on enlève la valeur 2 ; il reste 0 unité à rendre

   La combinaison est bien de trois unités, solution optimale.

#. Cet algorithme donne une solution mais elle n'est pas toujours optimale comme le montre l'exemple suivant.

   Prenons comme système monétaire les valeurs 1, 3, 6, 12, 24 et 30.

   a. Comment rendre la somme de 48 unités de manière optimisée ?

      En appliquant l'algorithme glouton, on obtient :

      -  on enlève la plus grande valeur possible 30 ; il reste 18 unités à rendre
      -  on enlève la plus grande valeur possible 12 ; il reste 6 unités à rendre
      -  on enlève la plus grande valeur possible 6 ; il reste 0 unité à rendre

      La solution donnée par l'algorithme glouton est 3 unités (30, 12 et 6). Elle n'est pas optimale car on peut rendre
      la somme de 48 unités avec 2 unitéss de valeur 24.


Programmation python
--------------------

Un algorithme glouton appliqué au problème du rendu de monnaie se présente ainsi : 

.. code-block:: text

   tableau des unités = [200, 100, 50, 20, 10, 5, 2, 1] (ordre croissant)
   nombre_unités = 0
   On prend la première pièce du tableau des unités (la plus grande)
   Tant que la somme à rendre est supérieure à 0:
      Si la pièce est plus grande que la somme à rendre:
         on la soustrait de la somme à rendre
         nombre_unités augmente de 1
      sinon:
         on passe à la pièce suivante

Il existe différentes écritures de cet algorithme en Python.

#. En utilisant une seule boucle ``while``:

   .. literalinclude:: ../python/glouton_cours.py
      :language: python
      :lines: 1-12
      :linenos:

   >>> rendu_monnaie(48)
   5

#. En utilisant 2 boucles imbriquées :

   .. literalinclude:: ../python/glouton_cours.py
      :language: python
      :lines: 15-23
      :linenos:

   >>> rendu_monnaie(48)
   5