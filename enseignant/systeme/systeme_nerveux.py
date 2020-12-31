def systeme_nerv():
    """ permet de récuperer les enquetes sur le systeme nerveux des patient"""

    print("\n")
    print("SYSTEME NERVEUX\n")
    
    # POUR LES CEPHALEES
    print("LE PATIENTE A T-IL DES CEPHALEES ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        cephalees = "POSITIF"
    else:
        cephalees = "NEGATIF"

    # POUR LES CONFUSION
    print("LE PATIENTE A T-IL DES CONFUSIONS ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        confusion = "POSITIF"
    else:
        confusion = "NEGATIF"

    # POUR LES CONVULSIONS
    print("LE PATIENTE A T-IL DES CONVULSIONS ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        convulsion = "POSITIF"
    else:
        convulsion = "NEGATIF"
    
    # POUR LE VERTIGE
    print("LE PATIENTE A T-IL LE VERTIGE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        vertige = "POSITIF"
    else:
        vertige = "NEGATIF"

    # POUR LES PARALYSIES
    print("LE PATIENTE A T-IL DES PARALYSIES ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        paralysie = "POSITIF"
    else:
        paralysie = "NEGATIF"

    # POUR LA PARAISIE
    print("LE PATIENTE A T-IL DE LA PARAISIE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        paraisie = "POSITIF"
    else:
        paraisie = "NEGATIF"
    
    # POUR LA PARESTHESIE
    print("LE PATIENTE A T-IL DE LA PARESTHESIE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        paresthesie = "POSITIF"
    else:
        paresthesie = "NEGATIF"
    
    # POUR L'HYPOESTHESIE
    print("LE PATIENTE A T-IL DE L'HYPOESTHESIE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        hypoesthesie = "POSITIF"
    else:
        hypoesthesie = "NEGATIF"
    
    # POUR L'ANESTHESIE'
    print("LE PATIENTE A T-IL DE L'ANESTHESIE' ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        anesthesie = "POSITIF"
    else:
        anesthesie = "NEGATIF"
    
    enquete_nerv = {
        "Cephalees":cephalees,
        "Confusion":confusion,
        "Convulsions":convulsion,
        "Vertiges":vertige,
        "Paralysie":paralysie,
        "Paraisie":paraisie,
        "Paresthesie":paresthesie,
        "Hypoesthesie":hypoesthesie,
        "Anesthesie":anesthesie
    }

    return enquete_nerv



def Examen_nerv():
    """ Cette methode definit les examens effectues sur le systeme nerveux """

    print(" INSPECTION DU SYSTEME NERVEUX\n")
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

    print(" PALPATION DU SYSTEME NERVEUX \n")
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
    
    print(" PERCUTION DU SYSTEME NERVEUXE \n")
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

    print(" AUSCULTATION DU SYSTEME NERVEUX \n")
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

    examen_nerv = {
        "Inspection du systeme nerveux":liste_inspection,
        "Palpation du systeme nerveux":liste_palpation,
        "Percution du systeme nerveux":liste_percution,
        "Auscultation du systeme nerveux":liste_auscultation
    }

    return examen_nerv 


