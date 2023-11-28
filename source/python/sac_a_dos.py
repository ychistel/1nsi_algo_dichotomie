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


def combinaison(tableau):
    combinaisons = [ [k+1,tableau[k]] for k in range(len(tableau))]
    n = 1
    debut_i = 0
    fin = len(tableau)
    while n < len(tableau):
        i = debut_i
        while i < fin:
            j = combinaisons[i][0]
            while j < len(tableau):
                c = list(combinaisons[i][1:])
                c.append(tableau[j])
                c = [j+1] + c
                combinaisons.append(c)
                j = j + 1
            i = i + 1
        n = n + 1
        debut_i = fin
        fin = len(combinaisons)
    return combinaisons

def remplir_sac(tableau,capacite_max=10):
    """
    Paramètres :
    - tableau contient les listes de dictionnaires représentant
    les différents objets.
    Retour
    la fonction renvoie la liste qui a la plus grande valeur sans
    dépasser la capacité du sac
    """
    masse_sac = 0
    valeur_sac = 0
    sac_a_dos = []
    for liste_objets in tableau:
        m = 0
        v = 0
        for objet in liste_objets[1:]:
            m += objet['masse']
            v += objet['valeur']
        if m <= capacite_max and v > valeur_sac:
            valeur_sac = v
            masse_sac = m
            sac_a_dos = liste_objets[1:]
    return (sac_a_dos,masse_sac,valeur_sac)
        
solution = remplir_sac(combinaison(objets))