def glouton(cible,source):
    # sol: liste qui contient les valeurs solutions
    sol = []
    # source triée par ordre croissant, dernière valeur la plus grande d'indice i
    i = len(source)-1
    # tant que cible positive et source non entièrement parcouru
    while cible >= 0 and i >= 0:
        # on sélectionne une valeur du tableau source
        val = source[i]
        if val <= cible:
            # on enlève la valeur à la cible
            cible = cible - val
            # on ajoute la valeur en solution
            sol.append(val)
        else:
            # on passe à la valeur suivante inférieure dans le tableau source
            i = i - 1
    return sol

s1 = glouton(29,[1,4,6,10])


