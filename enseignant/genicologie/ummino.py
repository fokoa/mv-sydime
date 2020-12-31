

def Groupe_sanguin():
    """ Cette méthode retourne le groupe sanguin du patient"""

    groupe = input("VEUILLEZ INDIQUER LE GROUPE SANGUIN DU PATIENT EN TAPANT A, B, AB ou O \n AU CAS OU VOUS NE CONNAISSEZ PAS ENTREZ 'I' POUR INDIQUER QUE C'EST INCONNU \n")

    if groupe == "A" or groupe == "a":
        groupe_sanguin = "GROUPE A"
    if groupe == "B" or groupe == "b":
        groupe_sanguin = "GROUPE B"
    if groupe == "AB" or groupe == "ab":
        groupe_sanguin = "GROUPE AB"
    if groupe == "O" or groupe == "o":
        groupe_sanguin = "GROUPE O"
    else:
        groupe_sanguin = "INCONNU"

    return groupe_sanguin



def Facteur_rhesus():
    """ Cette méthode retourne le facteur rhésus du patient"""
    facteur = input("VEUILLEZ INDIQUER LE FACTEUR RHESSUS DU PATIENT EN TAPANT + OU - \n AU CAS OU VOUS NE CONNAISSEZ PAS ENTREZ 'I' POUR INDIQUER QUE C'EST INCONNU\n")
    
    if facteur == "+":
        rhésus = "RHESUS +"
    if facteur == "-":
        rhésus  = "RHESUS -"
    else:
        rhésus = "INCONNU"

    return rhésus


def Electrophoreze():
    """ Cette méthode retourne l'électrophorèse du patient"""

    groupe = input("VEUILLEZ INDIQUER LE TYPE SANGUIN DU PATIENT EN TAPANT AA, AS OU SS  \n AU CAS OU VOUS NE CONNAISSEZ PAS ENTREZ 'I' POUR INDIQUER QUE C'EST INCONNU \n")
    if groupe == "AA" or groupe == "aa":
        type_elc = "AA"
    if groupe == "AS" or groupe == "as":
        type_elc = "AS"
    if groupe == "SS" or groupe == "ss":
        type_elc = "SS"
    else:
        type_elc = "INCONNU"

    return type_elc



def Serologie():
    """ Cette méthode permet de recupéré la sérologie du patient """

    ajouter_maladie = True
    liste = []

    while ajouter_maladie == True:
        maladie = input("INDIQUEZ LA MALADIE FAISANT PARTIR DE LA SEROLOGIE DU PATIENT: ")
        liste.append(maladie)

        ajouter = input("AVEZ-VOUS UN AUTRE MALADIE ?\n VEUILLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")
        if ajouter == 'O' or ajouter == 'o' :
            ajouter_maladie = True
        else:
            ajouter_maladie = False
    
    return liste



def Allergenes():
    """ Cette méthode permet de recupéré la liste d'allergenes du patient """

    ajouter_allergene = True
    liste  = []

    while ajouter_allergene == True:
        allergene = input("VEUILLEZ INDIQUER UN ALLERGENE DU PATIENT: ")
        liste.append(allergene)

        ajouter = input("LE PATIENT A T-IL D'AUTRES ALLERGENES ?\n VEUILLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")
        if ajouter == 'O' or ajouter == 'o' :
            ajouter_allergene = True
        else:
            ajouter_allergene = False
    
    return liste