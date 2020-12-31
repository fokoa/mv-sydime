def nb_grossesse():
    """ Cette methode permet de returner le nombre de grossesse d'une patiente"""

    nb_gross = -1
    while nb_gross < 0 :
        nb_gross = input("VEUILLEZ INDIQUER LE NOMBRE DE GROSSESSE DU PATIENT :")
        try :
            nb_gross = int(nb_gross)
        except ValueError :
            print("DESOLE MAIS LA VALEUR ENTRE N'EST PAS UN NOMBRE MAIS UN MOT\n")
            print("VEUILLEZ ENTRER UN NOMBRE POUR INDIQUER LE NOMBRE DE GROSSESSE DU PATIENT")
            nb_gross = -1
        if nb_gross < 0 :
            print("DESOLE MAIS LA VALEUR ENTRE EST NEGATIVE ! VEUILLEZ ENTRER UN NOMBRE A PARTIR DE 0 ")
    
    return nb_gross




def complication():
    """ Cette methode permet de returner le nombre de complications de grossesse d'une patiente"""
    nb_comp = -1
    while nb_comp < 0 :
        nb_comp = input("VEUILLEZ INDIQUEZ LE NOMBRE COMPLICATION DE GROSSESSE DU PATIENT : ")
        try :
            nb_comp = int(nb_comp)
        except ValueError :
            print("DESOLE MAIS LA VALEUR ENTRE N'EST PAS UN NOMBRE MAIS UN MOT\n")
            print("VEUILLEZ ENTRER UN NOMBRE POUR INDIQUER L'AGE DU PATIENT")
            nb_comp = -1
        if nb_comp < 0 :
            print("DESOLE MAIS LA VALEUR ENTRE EST NEGATIVE ! VEUILLEZ ENTRER UN NOMBRE A PARTIR DE 0 ")
    
    return nb_comp




def fausse_couche():
    """ Cette methode permet de returner le nombre de fausse couche d'une patiente"""
    nb_fausse = -1
    while  nb_fausse < 0 :
        nb_fausse = input("VEUILLEZ INDIQUEZ LE NOMBRE DE FAUSSE COUCHE DU PATIENT : ")
        try :
            nb_fausse = int( nb_fausse)
        except ValueError :
            print("DESOLE MAIS LA VALEUR ENTRE N'EST PAS UN NOMBRE MAIS UN MOT\n")
            print("VEUILLEZ ENTRER UN NOMBRE POUR INDIQUER L'AGE DU PATIENT")
            nb_fausse = -1
        if  nb_fausse < 0 :
            print("DESOLE MAIS LA VALEUR ENTRE EST NEGATIVE ! VEUILLEZ ENTRER UN NOMBRE A PARTIR DE 0 ")
    
    return nb_fausse



def maladi_grossesse():
    """ Cette methode permet de returner les maladies liées aux grossesses d'une patiente"""
    liste_maladieGr  = []

    print("LA PATIENTE A T-ELLE DES DES MALADIES LIEES A LA GROSSESSE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "N" or reponse == "n" :
        if len(liste_maladieGr) == 0:
            liste_maladieGr.append("AUCUNE")
            

    elif reponse == "O" or reponse == "o":
        ajouter_maladiGr = True
        while ajouter_maladiGr == True:
            maladie = input("VEUILLEZ INDIQUER LA MALADIE LIEE A LA GROSSESSE DU  DU PATIENT : ")
            liste_maladieGr.append(maladie)
            rajouter = input("PRESENTE T-ELLE D'AUTRES MALADIE? REPONDEZ PAR O/n : ")
            if rajouter == 'O' or rajouter == 'o':
                ajouter_maladiGr = True
            else:
                ajouter_maladiGr = False

    return liste_maladieGr


def maladie_genicologique():
    """ Cette methode permet de returner les maladies génicologiques d'un patient"""
    liste_maladieG  = []

    print("LA PATIENTE A T-ELLE DES DES MALADIES LIEES A LA GROSSESSE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "N" or reponse == "n" :
        if len(liste_maladieG) == 0:
            liste_maladieG.append("AUCUNE")
            

    elif reponse == "O" or reponse == "o":
        
        ajouter_maladiG = True
        while ajouter_maladiG == True:
            maladie = input("VEUILLEZ INDIQUER LA MALADIE GENICOLOGIQUE DU PATIENT \n")
            liste_maladieG.append(maladie)
            rajouter = input("Y A T-IL D'AUTRES MALADIES? REPONDEZ PAR O/n : ")
            if rajouter == 'O' or rajouter == 'o':
                ajouter_maladiG = True
            else:
                ajouter_maladiG = False
    
    return liste_maladieG

    
        