def systeme_sphere():
    """ permet de récuperer les enquetes sur le systeme des  sphères ORL des patient"""

    print("\n")
    print("SYSTEME SPHERE ORL\n")
    
    # POUR L'HYPOACCOUSIE
    print("LE PATIENTE A T-IL DE L'HYPOACCOUSIE?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        hypoaccousie = "POSITIF"
    else:
        hypoaccousie = "NEGATIF"

    # POUR L'ATODYNIE
    print("LE PATIENTE A T-IL DE L'ATODYNIE?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        atodynie = "POSITIF"
    else:
        atodynie = "NEGATIF"  

    # POUR L'OTALGIE
    print("LE PATIENTE A T-IL DE L'OTALGIE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        otalgie = "POSITIF"
    else:
        otalgie = "NEGATIF"
    
    # POUR L'OTORRAGIE
    print("LE PATIENTE A T-IL DE L'OTORRAGIE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        otorragie = "POSITIF"
    else:
        otorragie = "NEGATIF"
    
    # POUR L'OTALGIE
    print("LE PATIENTE A T-IL DE L'OTALGIE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        otalgie = "POSITIF"
    else:
        otalgie = "NEGATIF"    
    
    # POUR L'OACCOUSPHENE
    print("LE PATIENTE A T-IL DE L'ACCOUSPHENE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        accousphene = "POSITIF"
    else:
        accousphene = "NEGATIF"
    
    # POUR LA DYSPHONIE
    print("LE PATIENTE A T-IL DE LA DYSPHONIE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        dysphonie = "POSITIF"
    else:
        dysphonie = "NEGATIF"
    
    # POUR LA RHINORHEE
    print("LE PATIENTE A T-IL DE LA RHINORHEE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        rhinorhee = "POSITIF"
    else:
        rhinorhee = "NEGATIF"
    
    # POUR LA RHINORRAGIEE
    print("LE PATIENTE A T-IL DE LA RHINORRAGIE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        rhinorragie = "POSITIF"
    else:
        rhinorragie = "NEGATIF"
    
    # POUR LA RHINOLALIE
    print("LE PATIENTE A T-IL DE LA RHINOLALIE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        rhinolalie = "POSITIF"
    else:
        rhinolalie = "NEGATIF"

    # POUR L'EPISTAXIE
    print("LE PATIENTE A T-IL DE L'EPISTAXIE?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        epistaxie = "POSITIF"
    else:
        epistaxie = "NEGATIF"
    
    # POUR L'ANASMIE
    print("LE PATIENTE A T-IL DE L'ANASMIE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        anasmie = "POSITIF"
    else:
        anasmie = "NEGATIF"
    
    # POUR LA DYSOSMIE
    print("LE PATIENTE A T-IL DE LA DYSOSMIE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        dysosmie = "POSITIF"
    else:
        dysosmie = "NEGATIF"

    # POUR LA CACOSMIE
    print("LE PATIENTE A T-IL DE LA CACOSMIE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        cacosmie = "POSITIF"
    else:
        cacosmie = "NEGATIF"

    enquete_sphere = {
        "Hypoaccousie":hypoaccousie,
        "Atodynie":atodynie,
        "Otalgie":otalgie,
        "Otorragie":otorragie,
        "Accouphene":accousphene,
        "Dysphonie":dysphonie,
        "Rhinorhee":rhinorhee,
        "Rhinorragie":rhinorragie,
        "Rhinilalie":rhinolalie,
        "Epistaxie":epistaxie,
        "Anasmie":anasmie,
        "Dysosmie":dysosmie,
        "Cacosmie":cacosmie
    }

    return enquete_sphere



def Examen_sphere():
    """ Cette methode definit les examens effectues sur les spheres ORL """

    print(" INSPECTION DES SPHERES ORL \n")
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

    print(" PALPATION DES SPHERES ORL \n")
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

    print(" PERCUTION DES SPHERES ORL \n")
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

    print(" AUSCULTATION DES SPHERES ORL \n")
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

    examen_sphere = {
        "Inspection des spheres orl":liste_inspection,
        "Palpation des spheres orl":liste_palpation,
        "Percution des spheres orl":liste_percution,
        "Auscultation des spheres orl":liste_auscultation
    }

    return examen_sphere

       
    