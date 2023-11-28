def rendu_monnaie(somme_a_rendre):
    tableau_des_unites = [100,50,20,10,5,2,1]
    nombre_unites = 0
    i = 0
    piece = tableau_des_unites[i]
    while somme_a_rendre > 0:
        if somme_a_rendre >= piece:
            somme_a_rendre = somme_a_rendre - piece
            nombre_unites = nombre_unites + 1
        else:
            i = i + 1
            piece = tableau_des_unites[i]
    return nombre_unites

def rendu_monnaie(somme_a_rendre):
    """somme à rendre (int) -> nombre de pièces (int)"""
    pieces = [200,100,50,20,10,5,2,1]
    n = 0 # nombre pièces
    for p in pieces:
        while somme_a_rendre >= p:
            somme_a_rendre = somme_a_rendre - p
            n = n + 1
    return n