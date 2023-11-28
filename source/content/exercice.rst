Exercices sur la recherche par dichotomie
==========================================

Exercice 1
----------

Soit T le tableau trié ``T=[8, 8, 17, 21, 23, 27, 28, 45, 57, 71, 77, 84, 88, 95, 97]``

#. On recherche le nombre ``23`` dans le tableau T. Donner les différentes zones de recherche dans le tableau pour trouver ce nombre.
#. Combien d’itérations ont été nécessaires pour touver le nombre cherché ?
#. On cherche le nombre ``75``. Combien d'itérations doit-on prévoir pour vérifier qu'il n'est pas dans le tableau ``T``?

Exercice 2
----------

En vous inspirant de l'algorithme de recherche par dichotomie écrit en pseudo-code dans le cours, proposer une version en en langage Python.

Exercice 3
----------

On souhaite mesurer le temps de recherche d'un nombre dans un tableau trié. On reprend la fonction ``mesure`` (vue dans la partie sur les algorithmes de tri) pour mesurer la fonction de recherche par dichotomie.

.. literalinclude:: ../python/mesure.python
   :lines: 1-27

#. Compléter le code pour créer un tableau ``t`` ordonné de nombres. La construction sera effectuée avec un tableau par compréhension.
#. Associer une valeur à la variable ``v`` qui n'est pas dans le tableau ``t``.
#. Effectuer des mesures de recherche par dichotomie sur des tableaux de dimensions différentes.

   a. Compléter le tableau ci-dessous:

      +-------------+------+------+------+------+------+------+-------+
      | dimension n | 1000 | 2000 | 3000 | 4000 | 5000 | 8000 | 10000 |
      +-------------+------+------+------+------+------+------+-------+
      | temps en s  |      |      |      |      |      |      |       |
      +-------------+------+------+------+------+------+------+-------+
   
   b. Comment augmente le temps de recherche par rapport à la dimension ``n`` du tableau ?