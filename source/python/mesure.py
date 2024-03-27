from time import time

# ici code de la fonction de recherche dichotomique

def mesure(fct,n):
    """
    Paramètres :
    - fct : type str, nom de la fonction à mesurer
    - n : type int, dimension du tableau dans lequel se fait la recherche
    La fonction effectue 10 mesures de temps d'exécution de la fonction. 
    Le tableau t sur lequel se fait la recherche est créé par compréhension. 
    La valeur v à chercher dans le tableau est une valeur non présente dans le tableau.
    La fonction renvoie le temps moyen d'exécution pour chercher la valeur v dans le tableau t.
    """
    tps = 0.0
    
    for _ in range(10):
        # on crée un tableau t contenant les n premiers nombres entiers [1,2,3,...]
        t = ['...']
        # v valeur cherchée dans le tableau
        v = 0
        expression = fct + "(t,v)"
        
        # mesure du temps d'exécution de la fonction
        t_0 = time()
        eval(expression)
        t_1 = time()
        tps = tps + (t_1-t_0)
    
    # on renvoie le temps moyen d'exécution de la fonction
    return tps/10