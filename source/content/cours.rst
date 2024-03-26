Recherche dichotomique
======================

La **dichotomie** est un mot d'origine greque qui signifie "diviser en deux".

La recherche d'une valeur par dichotomie dans un tableau peut être facilitée si celui-ci est trié. Dans ce cas, on
divise successivement le tableau en 2 jusqu'à atteindre la valeur cherchée.

L'algorithme
------------

.. admonition:: Algorithme
   :class: algo
      
   L'algorithme de recherche dichotomique se fait dans un **tableau trié**. On définit plusieurs variables :

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

Appliquons cet algorithme pour rechercher la valeur 12 dans le tableau trié ``t=[5, 9, 12, 14, 15, 16, 19, 20, 23, 25]``. 

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

L'algorithme de recherche utilise une boucle. Comment être sûr que cette boucle se termine même si la valeur cherchée n'est pas dans le tableau ?

.. admonition:: Définition
   :class: definition

   On appelle **variant de boucle** une quantité entière qui est positive ou nulle et décroit strictement à chaque itération.

   Si on trouve une telle quantité dans une boucle, alors on est sûr que la boucle se termine.

.. rubric:: Preuve de la terminaison

Dans l'algorithme de **recherche par dichotomie**, le test ``deb < fin`` est équivalent au test ``fin - deb > 0``. Le nombre ``fin - deb`` est un variant de boucle.

- Le nombre ``fin - deb`` est strictement positif dans la boucle ``while``.
- Le nombre ``fin - deb`` décroît car à chaque itération. C'est soit l'indice ``deb`` qui augmente, soit l'indice ``fin`` qui diminue.

En conclusion, le nombre ``fin - deb`` est un **variant de boucle** positif qui décroit, assurant la terminaison de la boucle ``while`` de l'algorithme de recherche par dichotomie.

Complexité de l'algorithme
--------------------------

La recherche dichotomique s'applique sur un tableau trié de nombres. À chaque itération, la recherche se fait dans une partie du tableau dont la longueur est divisée par 2. Inévitablement, la longueur finit par être égale à 0.

Combien d'itérations faut-il pour obtenir une zone du tableau dont la longueur est 0 ?

Prenons en exemple un tableau trié contenant 50 valeurs. La zone de recherche est divisée en 2 à chaque itération ce qui donne des longueurs de 50, 25, 12, 6, 3, 1 et 0. On obtient une zone le longueur nulle en 6 itérations. 

Du point de vue mathématique, on peut remarquer que :math:`2^{5} = 32 < 50` et que :math:`2^{6} = 64 > 50`. Donc le nombre d'itérations correspond au plus petit exposant entier de 2 qui dépasse le nombre de valeurs dans le tableau.

.. admonition:: Propriété
   :class: propriete

   Le nombre d'itérations maximum pour chercher une valeur dans un tableau trié contenant ``n`` valeurs est le nombre entier ``p``, premier exposant du nombre 2 tel que :math:`2^{p} \geqslant n`.

   Le nombre ``p`` est le logarithme du nombre ``n`` en base 2 : :math:`p=\log_{2}(n)`

.. admonition:: Propriété
   :class: propriete

   La complexité de l'algorithme de recherche dichotomique est **logarithmique** et se note :math:`O(\log_{2}(n))`. 
   
   Cette complexité est une complexité dans le pire des cas, c'est à dire lorsque le nombre cherché n'est pas dans le tableau.

   La complexité logarithmique est plus efficace que la complexité linéaire : :math:`O(\log_{2}(n)) < O(n)`

Par exemple, un tableau trié contient 200 nombres, en supposant le pire des cas, c'est à dire que le nombre cherché n'est pas dans le tableau, nécessite au moins 8 itérations car :math:`2^{8} = 256 > 200`.

.. hint::

   On peut calculer le logarithme en base 2 d'un nombre en Python:

   >>> from math import log2
   >>> log2(200)
   7.643856189774724

   Ce résultat confirme qu'il faut 8 itérations pour montrer que le nombre cherché n'est pas dans le tableau.
