def systeme_cardio():
    """ permet de récuperer les enquetes sur le systeme cardiovasculaire des patient"""
    
    print("\n")
    print("SYSTEME CARDIOVASCULAIRE\n")
    
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
    
    # POUR LES ORTHOPNEE
    print("LE PATIENTE FAIT T-IL DE ORTHOPNEE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        orthopnee = "POSITIF"
    else:
        orthopnee = "NEGATIF"
    
    # POUR LA SYRCOPE
    print("LE PATIENTE A T-IL DES SYNCOPE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        syncope = "POSITIF"
    else:
        syncope = "NEGATIF"

    # POUR LA LIPOTHYMIE
    print("LE PATIENTE A T-IL DE LA LIPOTHYMIE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        lipothymie = "POSITIF"
    else:
        lipothymie = "NEGATIF"
    
    # POUR LES PALPITATIONS
    print("LE PATIENTE A T-IL DES PALPITATIONS ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        palpitations = "POSITIF"
    else:
        palpitations = "NEGATIF"
    
    # POUR LES HEPATALGIE
    print("LE PATIENTE A T-IL DE L'HEPATALGIE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        hepatalgie = "POSITIF"
    else:
        hepatalgie = "NEGATIF"
    
    enquete_cardio = {
        "Douleurs Thoracique":douleurs_th,
        "Dyspnee":dyspnees,
        "Orthopnee":orthopnee,
        "Syncope":syncope,
        "Lipothymie":lipothymie,
        "Palpitations":palpitations,
        "Hepatalgie":hepatalgie
    }
    
    return enquete_cardio


    

def Examen_cardio():
    """ Cette methode definit les examens effectues sur le systeme cardiaque """

    print(" INSPECTION DU SYSTEME CARDIAQUE \n")
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

    
    print(" PALPATION DU SYSTEME CARDIAQUE \n")
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

    
    print(" PERCUTION DU SYSTEME CARDIAQUE \n")
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



    print(" AUSCULTATION DU SYSTEME CARDIAQUE \n")
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


    examen_cardio = {
        "Inspection du systeme cardiaque":liste_inspection,
        "Palpation du systeme cardiaque":liste_palpation,
        "Percution du systeme cardiaque":liste_percution,
        "Auscultation du systeme cardiaque":liste_auscultation
    }

    return examen_cardio  