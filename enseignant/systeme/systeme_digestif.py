def systeme_digestif():
    """ permet de récuperer les enquetes sur le systeme digestif des patient"""

    print("\n")
    print("SYSTEME DIGESTIF\n")
    
    # POUR LES DOULEURS ABDOMINALES
    print("LE PATIENTE A T-IL DES DOULEURS ABDOMINALES ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        douleurs_ab = "POSITIF"
    else:
        douleurs_ab = "NEGATIF"

    # POUR LES NAUSEES
    print("LE PATIENTE A T-IL DES NAUSEES ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        nausees = "POSITIF"
    else:
        nausees = "NEGATIF"    

    # POUR LES VOMISSEMENTS
    print("LE PATIENTE FAIT T-IL DES VOMISSEMENTS ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        vomissement = "POSITIF"
    else:
        vomissement = "NEGATIF"    

    # POUR LA DYPHAGIE
    print("LE PATIENTE A T-IL DE LA DYPHAGIE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        dyphagie = "POSITIF"
    else:
        dyphagie = "NEGATIF" 

    # POUR LES ODYNOPHAGIE
    print("LE PATIENTE A T-IL DES ODYNOPHAGIES ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        odynophagie = "POSITIF"
    else:
        douleurs_ab = "NEGATIF"
    
    # POUR LA DYSPEPSIE
    print("LE PATIENTE A T-IL DE LA DYSPEPSIE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        dyspepesie = "POSITIF"
    else:
        dyspepesie = "NEGATIF"
    
    # POUR LES HEMATEMESES
    print("LE PATIENTE A T-IL DES HEMATEMESES ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        hematemese = "POSITIF"
    else:
        hematemese = "NEGATIF"
    
    # POUR LES PYROSIS
    print("LE PATIENTE A T-IL DES PYROSIS ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        pyrosis = "POSITIF"
    else:
        pyrosis = "NEGATIF"
    
    # POUR LES DIARHEE
    print("LE PATIENTE A T-IL DES DIARHEES ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        diarhee = "POSITIF"
    else:
        diarhee = "NEGATIF"
    
    # POUR LES CONSTIPATIONS
    print("LE PATIENTE A T-IL DES CONSTIPATIONS ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        constipations = "POSITIF"
    else:
        constipations = "NEGATIF"
    
    # POUR LES EPREINTES
    print("LE PATIENTE A T-IL DES EPREINTES ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        epreintes = "POSITIF"
    else:
        epreintes = "NEGATIF"
    
    # POUR LES TENESMES
    print("LE PATIENTE A T-IL DES TENESMES ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        tenesme = "POSITIF"
    else:
        tenesme = "NEGATIF"
    
    # POUR LES FAUX BESOINS
    print("LE PATIENTE A T-IL DES FAUX BESOINS ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        faux_b = "POSITIF"
    else:
        faux_b = "NEGATIF"
    
    # POUR LES MELENA
    print("LE PATIENTE A T-IL DE LA MELENA ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        melena = "POSITIF"
    else:
        melena = "NEGATIF"
    
    # POUR LES RECTORRAGIE
    print("LE PATIENTE A T-IL DE LA RECTORRAGIE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        rectorragie = "POSITIF"
    else:
        rectorragie = "NEGATIF"
    
    # POUR L'ODYNOPHAGIE
    print("LE PATIENTE A T-IL DE L'ODYNOPHAGIE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        odynophagie = "POSITIF"
    else:
        odynophagie = "NEGATIF"
    
    enquete_digestif = {
        "Douleurs abdominales":douleurs_ab,
        "Nausees":nausees,
        "Vomissements":vomissement,
        "Dysphagie":dyphagie,
        "Odynophagie":odynophagie,
        "Dyspepsie":dyspepesie,
        "Hematemese":hematemese,
        "Pyrosis":pyrosis,
        "Diarhée":diarhee,
        "Constipation":constipations,
        "Epreintes":epreintes,
        "Tenesme":tenesme,
        "Faux Besoins":faux_b,
        "Melena":melena,
        "Rectorragie":rectorragie
    }

    return enquete_digestif
    


def Examen_digestif():
    """ Cette methode definit les examens effectues sur le systeme digestif """

    print(" INSPECTION DU SYSTEME DIGESTIF \n")
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
    
    print(" PALPATION DU SYSTEME DIGESTIF \n")
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

    print(" PERCUTION DU SYSTEME DIGESTIF \n")
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

    print(" AUSCULTATION DU SYSTEME DIGESTIF \n")
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

    examen_digestif = {
        "Inspection du systeme digestif":liste_inspection,
        "Palpation du systeme digestif":liste_palpation,
        "Percution du systeme digestif":liste_percution,
        "Auscultation du systeme digestif":liste_auscultation
    }

    return examen_digestif

