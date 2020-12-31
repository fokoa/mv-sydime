def systeme_hema():
    """ permet de récuperer les enquetes sur le systeme nerveux des patient"""

    print("\n")
    print("SYSTEME HEMATOPOIETIQUE\n")
    
    # POUR L'ASTHENIE
    print("LE PATIENTE A T-IL DE LA FATIGUE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        asthenie = "POSITIF"
    else:
        asthenie = "NEGATIF"

    # POUR LA PALEUR
    print("LE PATIENTE A T-IL DE LA PALEUR ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        paleur = "POSITIF"
    else:
        paleur = "NEGATIF"

    enquete_hema = {
        "Asthenie":asthenie,
        "Paleur":paleur
    }

    return enquete_hema



def Examen_hema():
    """ Cette methode definit les examens effectues sur le systeme hematopoietique """

    print(" INSPECTION DU SYSTEME HEMATOPOIETIQUE \n")
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

    print(" PALPATION DU SYSTEME HEMATOPOIETIQUE \n")
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

    print(" PERCUTION DU SYSTEME HEMATOPOIETIQUE \n")
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

    print(" AUSCULTATION DU SYSTEME HEMATOPOIETIQUE \n")
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

    examen_hema = {
        "Inspection du systeme hematopoietique":liste_inspection,
        "Palpation du systeme hematopoietique":liste_palpation,
        "Percution du systeme hematopoietique":liste_percution,
        "Auscultation du systeme hematopoietique":liste_auscultation
    }

    return examen_hema 


