from time import time

def mesure(fct,n):
    """
    Paramètres :
    - fct : type str, nom de la fonction à mesurer
    - n : type int, dimension du tableau dans lequel se fait la recherche
    Script :
    on effectue 50 mesures de temps d'exécution de la fonction. Le tableau t sur lequel se fait la recherche est créé par compréhension. La valeur v à chercher dans le tableau est une valeur non présente dans le tableau.
    La fonction renvoie le temps moyen d'exécution pour chercher la valeur v dans le tableau t.
    """
    tps = 0.0
    
    for _ in range(50):
        t = ['...']
        v = 0
        expression = fct + "(t,v)"
        
        # mesure du temps
        t_0 = time()
        eval(expression)
        t_1 = time()
        tps = tps + (t_1-t_0)
    
    # on renvoie le temps moyen d'exécution de la fonction
    return tps/50
