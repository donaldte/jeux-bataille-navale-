#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy as np

def correspondance_case(table, i, j):
    if not isinstance(table,np.ndarray):
        return "le tableau doit etre defini grace a numpy"
    
    # verifions que le tableau soit de type 10x10
    
    if not table.shape == (10,10):
        return "le tableau doit etre de type 10x10"
    
    # verifions que le tableau ne contient que des 1 et ou des 0
    
    for i in range(10):
        for j in range(10):
            if not table[i][j] in [0,1]:
                return "la table ne doit contenir que des 0 et ou des 1"
    
    
    # verifions si i et j sont des entiers naturels compris entre 0 et 9 inclus
    if (not i in range(10)) or (not j in range(10)):
                                 return "les coordonnees doivent toutes etre des entiers naturels tous compris entre 0 et 9 inclus"
                                 
    # verification de la nature de la case en qustion
    
    if table[i][j] == 1:
        return "bateau"
    else:
        return "eau"
    

# difinition de la fonction permettant de dire si un navir a ete touche et s'il a coule ou pas

def bataille_navale(table):
    # demandons au joueur d'entrer les coordonnees de sa cible
    
    l =int (input("entrer le numero de la ligne de votre cible compris entre 0 et 9 inclus"))
    c = int (input("entrer le numero de la colonne de votre cible compris entre 0 et 9 inclus"))
    droite, gauche, dessus, dessous = False, False, False, False
            
    # comptons le nombre de cases contenant 1
    n=0
            
    for i in range(10):
            for j in range(10):
                    if table[i][j] == 1:
                            n += 1
            
            
    # cas ou la cible touchee est un bateau,c'est a dire que cette case contient 1
    if table[l][c] == 1:
            n -= 1
            table[l][c] = 2
            c_sup = c
            c_inf = c
        # verifions si le bateau est de type ligne
            if c+1 < 10:
                for i in range(c,10):
                    if table[l][i] in [2,1]:
                        c_sup = i
                    else:
                        break
                if c_sup != c:
                    droite = True
            else:
                c_sup = c
            
            if c-1 > 0:
                for i in range(c,-1,-1):
                    if table[l][i] in [2,1]:
                        c_inf = i
                    else: break
                if c_inf != c:
                    gauche = True        
            else: 
                c_inf = c
        
        # verifions si le batteau est de type colonne
            if l+1 < 10:
                for i in range(l,10):
                    if table[i][c] in [2,1]:
                        l_sup = i
                    else:
                        break
                if l_sup != c:
                    dessous = True        
            else:
                l_sup = l
            
            if l-1 > 0:
                for i in range(l,-1,-1):
                    if table[i][c] in [2,1]:
                        l_inf = i
                    else: break
                if l_inf != c:
                    dessus = True        
            else: 
                l_inf = l
            
         # verifions si le navir touche a coule ou pas
            t = True
            if droite==True or gauche==True:
                t=False
                f = 0

                for i in range(c_inf,c_sup+1):
                            if table[l][i] == 2:
                                f += 1
                if f == c_sup - c_inf+1 :
                        print("navir coule")
                        print(table)
                else: 
                    print("navir touche")
                    print(table)
                    
            if t:
                if dessus==True or dessous==True:
                    t = True

                    f = 0

                    for i in range(l_inf,l_sup+1):
                            if table[i][c] == 2:
                                f += 1
                    if f == l_sup - l_inf +1:
                            print("navir coule")
                            print(table)
                    else:
                        print("navir touche")
                        print(table)
                
      
            
    elif table[l][c]==2:
        print("Partie du bateau deja touchee")
        print(table)
        
    else:    
        print("cible manquee")
        table[l][c] = -1
        print(table)
        
    if n == 0:
            print("felicitation tous les navirs ont ete coules")
            
            
        
            
    
            
            
            
            
            
            
            
            
    
                        


# In[20]:


# test de la fonction precedemment definie

table = np.zeros((10,10))
table[0][8] = 1
table[3][7] = 1
table[4][7] = 1
table[9][9] = 1
print(table)

correspondance_case(table,0,8)


# In[22]:


bataille_navale(table)


# In[ ]:




