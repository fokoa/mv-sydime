def systeme_pul():
    """ permet de récuperer les enquetes sur le systeme pulmonaire des patient"""

    print("\n")
    print("SYSTEME PULMONAIRE\n")

    # POUR LES DOULEURS THORACIQUES
    print("LE PATIENTE A T-IL DES DOULEURS THORACIQUES ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        douleurs_th = "POSITIF"
    else:
        douleurs_th = "NEGATIF"    

    # POUR LES DYSPSEES
    print("LE PATIENTE A T-IL DES DYSPNEES?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        dyspnees = "POSITIF"
    else:
        dyspnees = "NEGATIF"
    
    # POUR LES EXPECTORATION-BRONCHORRHEE
    print("LE PATIENTE FAIT T-IL DES EXPECTORATION-BRONCHORRHEE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        expectoration = "POSITIF"
    else:
        expectoration = "NEGATIF"

    # POUR LA TOUX
    print("LE PATIENTE A T-IL DE LA TOUX ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        toux = "POSITIF"
    else:
        toux = "NEGATIF"

    # POUR LES HEMOPHYSES
    print("LE PATIENTE A T-IL DE L'HEMOPHYSIE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        hemophysie = "POSITIF"
    else:
        hemophysie = "NEGATIF"
    

    # POUR LA VOMIQUE
    print("LE PATIENTE A T-IL DE LA VOMIQUE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        vomique = "POSITIF"
    else:
        vomique = "NEGATIF"
    
    # POUR LES HOQUET
    print("LE PATIENTE A T-IL DU HOQUET ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        hoquet = "POSITIF"
    else:
        hoquet = "NEGATIF"
    
    # POUR LA VOIX BITONALES
    print("LE PATIENTE A T-IL UNE VOIX BITONALE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        voix_b = "POSITIF"
    else:
        voix_b = "NEGATIF"
    
    # POUR LA VOIX ROQUE
    print("LE PATIENTE A T-IL LA VOIX ROQUE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        roque = "POSITIF"
    else:
        roque = "NEGATIF"

    # POUR LES RONFLEMENTS
    print("LE PATIENTE A T-IL DES RONFLEMENTS ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        ronflement = "POSITIF"
    else:
        ronflement = "NEGATIF"

    enquete_pul = {
        "Douleur Thoracique":douleurs_th,
        "Dyspnee":dyspnees,
        "Expectoration-Bronchorrhee":expectoration,
        "Toux":toux,
        "Hemophysie":hemophysie,
        "Vomique":vomique,
        "Hoquet":hoquet,
        "Voix Bitonique":voix_b,
        "Voix Roque":roque,
        "Ronflement":ronflement
    }

    return enquete_pul
    

    
def Examen_pul():
    """ Cette methode definit les examens effectues sur le systeme pulmonaire """

    print(" INSPECTION DU SYSTEME PULMONAIRE\n")
    ajouter_inspection = True
    liste_inspection = []

    while ajouter_inspection == True:
        inspection = input("INDIQUEZ LA REMARQUE FAIT LORS DE L'INSPECTION DU PATIENT: ")
        liste_inspection.append(inspection)

        ajouter = input("AVEZ-VOUS UNE AUTRE REMARQUE ?\n VEUILLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")
        if ajouter == 'O' or ajouter == 'o' :
            ajouter_inspection= True
        else:
            ajouter_inspection = False

    print(" PALPATION DU SYSTEME PULMONAIRE \n")
    ajouter_palpation = True
    liste_palpation = []

    while ajouter_palpation == True:
        palpation = input("INDIQUEZ LA REMARQUE FAIT LORS DE LA PALPATION DU PATIENT: ")
        liste_palpation.append(palpation)

        ajouter = input("AVEZ-VOUS UNE AUTRE REMARQUE ?\n VEUILLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")
        if ajouter == 'O' or ajouter == 'o' :
            ajouter_palpation = True
        else:
            ajouter_palpation = False
    
    print(" PERCUTION DU SYSTEME PULMONAIRE \n")
    ajouter_percution = True
    liste_percution = []

    while ajouter_percution == True:
        percution = input("INDIQUEZ LA REMARQUE FAIT LORS DE LA PERCUTION DU PATIENT: ")
        liste_percution.append(percution)

        ajouter = input("AVEZ-VOUS UNE AUTRE REMARQUE ?\n VEUILLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")
        if ajouter == 'O' or ajouter == 'o' :
            ajouter_percution = True
        else:
            ajouter_percution = False

    print(" AUSCULTATION DU SYSTEME PULMONAIRE \n")
    ajouter_auscultation = True
    liste_auscultation = []

    while ajouter_auscultation == True:
        auscultation = input("INDIQUEZ LA REMARQUE FAIT LORS DE L'AUSCULTATION DU PATIENT: ")
        liste_auscultation.append(auscultation)

        ajouter = input("AVEZ-VOUS UNE AUTRE REMARQUE ?\n VEUILLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")
        if ajouter == 'O' or ajouter == 'o' :
            ajouter_auscultation = True
        else:
            ajouter_auscultation = False

    examen_pul = {
        "Inspection du systeme pulmonaire":liste_inspection,
        "Palpation du systeme pulmonaire":liste_palpation,
        "Percution du systeme pulmonaire":liste_percution,
        "Auscultation du systeme pulmonaire":liste_auscultation
    }

    return examen_pul


