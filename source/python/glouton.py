def rendu_monnaie_1(somme_a_rendre):
    """somme à rendre (int) -> nombre de pièces (int)"""
    pieces = [200,100,50,20,10,5,2,1]
    n = 0 # nombre pièces
    for p in pieces:
        while somme_a_rendre >= p:
            somme_a_rendre = somme_a_rendre - p
            n = n + 1
    return n

def rendu_monnaie_2(somme_a_rendre):
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

def rendu_monnaie_3(somme_a_rendre):
    """somme à rendre (int) -> liste de pièces (list)"""
    pieces = [200,100,50,20,10,5,2,1]
    tab = [] # pièces utilisées
    for p in pieces:
        while somme_a_rendre >= p:
            somme_a_rendre = somme_a_rendre - p
            tab.append(p) # on ajoute la pièce à la liste
    return tab

def rendu_monnaie_4(somme_a_rendre):
    """solution 2 : on itère seulement sur la somme à rendre"""
    pieces = [200,100,50,20,10,5,2,1]
    tab = []
    i = 0
    while somme_a_rendre > 0:
        piece = pieces[i]
        if somme_a_rendre >= piece:
            somme_a_rendre = somme_a_rendre - piece
            tab.append(piece)
        else:
            i = i + 1
    return tab

def rendu_monnaie_rec(somme_a_rendre,i=0):
    """ algorithme récursif
        somme à rendre diminuée à chaque appel ou
        indice augmenté pour nouvelle pièce
        la fonction renvoie le nombre de pièces utilisées
    """
    pieces = [200,100,50,20,10,5,2,1]
    if somme_a_rendre == 0:
        return 0
    else:
        if somme_a_rendre >= pieces[i]:
            return 1 + rendu_monnaie_rec(somme_a_rendre - pieces[i],i)
        else:
            return rendu_monnaie_rec(somme_a_rendre,i+1)
        
def rendu_monnaie_rec2(somme_a_rendre,i=0):
    """ algorithme récursif
        somme à rendre diminuée à chaque appel ou
        indice augmenté pour nouvelle pièce
        la fonction renvoie la liste des pièces utilisées
    """
    pieces = [200,100,50,20,10,5,2,1]
    if somme_a_rendre == 0:
        return []
    else:
        if somme_a_rendre >= pieces[i]:
            return [pieces[i]] + rendu_monnaie_rec2(somme_a_rendre - pieces[i],i)
        else:
            return rendu_monnaie_rec2(somme_a_rendre,i+1)
        
if __name__ == '__main__':
    n = rendu_monnaie_2(48)
    print(n)