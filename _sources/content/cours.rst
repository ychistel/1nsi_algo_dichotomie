Recherche dichotomique
======================

La **dichotomie** est un mot d'origine greque qui signifie "diviser en deux".

La recherche d'une valeur par dichotomie dans un tableau peut être facilitée si celui-ci est trié. Dans ce cas, on
divise successivement le tableau en 2 jusqu'à atteindre la valeur cherchée.

L'algorithme
------------

Voici une écriture de l'algorithme de recherche dichotomique dans un **tableau trié** :

-  ``t`` désigne un tableau trié
-  ``v`` est la valeur cherchée dans le tableau
-  ``deb``, ``fin`` et ``mil`` sont les indices de position des valeurs dans le tableau.

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

.. admonition:: Exemple

   On cherche la valeur 12 dans le tableau trié ``t=[5, 9, 12, 14, 15, 16, 19, 20, 23, 25]``. 

   #. Première itération
   
      -  ``deb = 0`` et ``fin = 9`` donc ``deb < fin``, première itération de la boucle tant que ;
      -  on calcule la valeur de l'indice situé au milieu du tableau : ``mil=(0+9)//2=4``;
      -  La valeur cherchée ``12 < t[4] = 15`` se situe dans le tableau entre les indices ``deb=0`` et ``fin=mil-1=3``.

      .. image:: ../img/dicho_1.svg
         :alt: dicho_1.svg
         :align: center
   
   #. Deuxième itération
   
      -  ``deb = 0`` et ``fin = 3`` donc ``deb < fin``, deuxième itération de la boucle tant que;
      -  on calcule la valeur de l'indice situé entre les indices 0 et 3 : ``mil = (0+3)//2 = 1``;
      -  La valeur cherchée ``12 > t[1] = 9`` se situe dans le tableau entre les indices ``deb = mil+1 = 2`` et ``fin = 3``.

      .. image:: ../img/dicho_2.svg
         :alt: dicho_2.svg
         :align: center

   #. Troisième itération
   
      - ``deb = 2`` et ``fin = 3`` donc ``deb < fin``, troisième itération de la boucle tant que;
      -  on calcule la valeur de l'indice situé entre les indices 2 et 3 : ``mil = (2+3)//2 = 2``;
      -  La valeur cherchée ``12 = t[2]`` donc la valeur est dans le tableau et a pour indice 2.

      .. image:: ../img/dicho_3.svg
         :alt: dicho_3.png
         :align: center

Terminaison de l'algorithme
---------------------------

On appelle **variant de boucle** une quantité entière qui est positive ou nulle et décroit strictement à chaque itération.

Si on trouve une telle quantité dans une boucle while, celle-ci se termine.

.. rubric:: Preuve de la terminaison
   :name: preuve-de-la-terminaison

Dans l'algorithme de **recherche par dichotomie**, le test ``deb < fin`` est équivalent à ``fin - deb > 0``. Le nombre ``fin - deb`` est un variant de boucle.

- Le nombre ``fin - deb`` est strictement positif dans la boucle ``while``.
- De plus, le nombre ``fin - deb`` décroît car à chaque itération, soit c'est l'indice ``deb`` qui augmente, soit c'est le nombre ``fin`` qui diminue.

En conclusion, le nombre ``fin - deb`` est un **variant de boucle** positif qui décroit, assurant la terminaison de la boucle ``while`` de l'algorithme de recherche par dichotoime.

Complexité de l'algorithme
--------------------------

La recherche dichotomique s'applique sur un tableau trié de nombres.

Au départ, on compare le nombre cherché N avec la valeur du nombre M situé au milieu du tableau.

-  S'il est inférieur, N<M, alors on cherche le nombre N dans la première moitié du tableau.
-  S'il est supérieur, N>M, alors on cherche le nombre N dans la seconde moitié du tableau.

On recommence la recherche dans un tableau dont la longueur est divisée par 2. Dans le pire des cas, si le nombre cherché n'est pas dans le tableau, alors celui-ci est vide à la fin de la recherche.

Le nombre d'itérations `p` nécessaires pour vérifier la présence du nombre cherché vérifie la relation 
:math:`2^{p} \geqslant n` où ``n`` est la longueur initiale du tableau.

.. math::

   2^{p} \geqslant n & \Longleftrightarrow log(2^{p}) \geqslant log(n) \\
   & \Longleftrightarrow  p \times log(2) \geqslant log(n) \\
   & \Longleftrightarrow p \geqslant \dfrac{log(n)}{log(2)} \\
   & \Longleftrightarrow p \geqslant log_{2}(n)

donc le nombre de comparaison :math:`p` est supérieur ou égal à :math:`log_{2}(n)` dans le pire des cas.

La complexité de l'algorithme de recherche dichotomique est **logarithmique** : :math:`O(log_{2}(n))`.

.. admonition:: Exemple

   Pour un tableau trié contenant 20 nombres, en supposant le pire des cas, c'est à dire que le nombre cherché n'est pas dans le tableau, on cherche successivement dans un tableau de longueur 20, puis un tableau de longueur 9, puis de longueur 4, de longueur 2 et finalement un tableau à 1 élément.

   Cela implique, dans le pire des cas, 5 itérations de la boucle while. En calculant dans une console Python ``log2(20)`` on obtient environ ``4.32`` soit les 5 itérations attendues.' 

   >>> from math import log2
   >>> log2(20)
   4.321928094887363
