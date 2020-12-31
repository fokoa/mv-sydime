def hypothese():
    """ Cette methode permet de fournir les hypotheses de diagnostic """

    print(" PRESENTATION DES HYPOTHESES DE DIAGNOSTIC DU PATIENT \n")
    ajouter_hypothese = True
    liste_hypothese = []

    while ajouter_hypothese == True:

        diag_pos = input("INDIQUEZ LA MALADIE LA PLUS PROBABLE DONC PEUT SOUFFRIR LE PATIENT: ")

        origine = input("INDIQUEZ L'ORIGINE DE LA MALADIE")

        cause = input("INDIQUEZ LA CAUSE DE LA MALADIE")

        liste = []

        print("Y A T-IL UNE MALADIE POUVANT INDUIRE EN ERREUR ?")
        reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

        if reponse == "N" or reponse == "n" :
            if len(liste) == 0:
                liste.append("AUCUNE")
                
        elif reponse == "O" or reponse == "o":            
            ajouter_maladi = True
            while ajouter_maladi == True:
                maladie = input("VEUILLEZ INDIQUER LA MALADIE \n")
                liste.append(maladie)
                rajouter = input("Y A T-IL D'AUTRES MALADIES? REPONDEZ PAR 'O' POUR OUI ET 'n' POUR NON : ")
                if rajouter == 'O' or rajouter == 'o':
                    ajouter_maladi = True
                else:
                    ajouter_maladi = False

        hypothese = {
            "le diagnostic positf probable":diag_pos,
            "le diagnostic etiologique probable":{
                "origine de la maladie":origine,
                "la cause":cause
            },
            "le diagnostic differentiel":liste
        }
        
        liste_hypothese.append(hypothese)

        ajouter = input("AVEZ-VOUS UNE AUTRE HYPOTHESE ?\n VEUILLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")
        if ajouter == 'O' or ajouter == 'o' :
            ajouter_hypothese = True
        else:
            ajouter_hypothese = False

    return liste_hypothese


def diag_travail():
    """ Cette methode  fournir le de diagnostic de travail """

    print(" PRESENTATION DU DIAGNOSTIC DE TRAVAIL DU PATIENT \n")
    diag_pos = input("INDIQUEZ LA MALADIE DU PATIENT: ")
    origine = input("INDIQUEZ L'ORIGINE DE LA MALADIE")
    cause = input("INDIQUEZ LA CAUSE DE LA MALADIE")
    diagnostic = {
        "le diagnostic positf probable":diag_pos,
        "le diagnostic etiologique probable":{
            "origine de la maladie":origine,
            "la cause":cause
        }
    }

    return diagnostic

    