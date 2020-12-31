def systeme_geni():
    """ permet de récuperer les enquetes sur le systeme nerveux des patient"""

    print("\n")
    print("SYSTEME GENITAL\n")
    
    # POUR LA DYSPAREUNIE
    print("LE PATIENTE A T-IL DE LA DYSPAREUNIE?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        dyspareunie = "POSITIF"
    else:
        dyspareunie = "NEGATIF"

    # POUR LA DYSMERONHEE
    print("LE PATIENTE A T-IL DE LA DYSMERONHEE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        dysmeronhee = "POSITIF"
    else:
        dysmeronhee = "NEGATIF"

    # POUR LA MENOMAGIE
    print("LE PATIENTE A T-IL DE LA MENOMAGIE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        menomagie = "POSITIF"
    else:
        menomagie = "NEGATIF"

    # POUR LA METROMAGIE
    print("LE PATIENTE A T-IL DE LA METROMAGIE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        metromagie = "POSITIF"
    else:
        metromagie = "NEGATIF"

    # POUR LA LEUCORRHEE
    print("LE PATIENTE A T-IL DE LA LEUCORRHEE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        leucorrhee = "POSITIF"
    else:
        leucorrhee = "NEGATIF"

    # POUR LA MASTODYNIE
    print("LE PATIENTE A T-IL DE LA MASTODYNIE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        mastodynie = "POSITIF"
    else:
        mastodynie = "NEGATIF"

    # POUR LA GALACTORHEE
    print("LE PATIENTE A T-IL DE LA GALACTORHEE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        galactorhee = "POSITIF"
    else:
        galactorhee = "NEGATIF"

    enquete_geni = {
        "Dyspareunie":dyspareunie,
        "Dysmeronhee":dysmeronhee,
        "Menomagie":menomagie,
        "Metromagie":metromagie,
        "Leucorrhee":leucorrhee,
        "Mastodynie":mastodynie,
        "Galactorhee":galactorhee
    }
    
    return enquete_geni

    
def Examen_geni():
    """ Cette methode definit les examens effectues sur le systeme genital """

    print(" INSPECTION DU SYSTEME GENITAL \n")
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

    print(" PALPATION DU SYSTEME GENITAL \n")
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

    
    print(" PERCUTION DU SYSTEME GENITAL \n")
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

    print(" AUSCULTATION DU SYSTEME GENITAL \n")
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

    examen_geni= {
        "Inspection du systeme genital":liste_inspection,
        "Palpation du systeme genital":liste_palpation,
        "Percution du systeme genital":liste_percution,
        "Auscultation du systeme genital":liste_auscultation
    }

    return examen_geni


