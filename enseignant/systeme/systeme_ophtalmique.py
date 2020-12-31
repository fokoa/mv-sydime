def systeme_oph():
    """ permet de récuperer les enquetes sur le systeme ophtamique des patient"""

    print("\n")
    print("SYSTEME OPHTALMIQUE\n")
    
    # POUR LES MYODESOPSIES
    print("LE PATIENTE A T-IL DES MYODESOPSIES ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        myodesopsie = "POSITIF"
    else:
        myodesopsie = "NEGATIF"

    # POUR LES METAMORPHERIES
    print("LE PATIENTE A T-IL DES METAMORPHERIES?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        metamorpherie = "POSITIF"
    else:
        metamorpherie = "NEGATIF"

    # POUR LES PHOSPHENES
    print("LE PATIENTE FAIT T-IL DES PHOSPHENES ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        phosphene = "POSITIF"
    else:
        phosphene = "NEGATIF"
    
    # POUR LA PHOTOPHOBIE
    print("LE PATIENTE A T-IL DE LA PHOTOPHOBIE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        photophobie = "POSITIF"
    else:
        photophobie = "NEGATIF"

    # POUR LES LARMOIEMENT
    print("LE PATIENTE A T-IL DES LARMOIEMENT ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        larmoiement = "POSITIF"
    else:
        larmoiement = "NEGATIF"
    
    # POUR LES DOULEURS OCCULAIRES
    print("LE PATIENTE A T-IL DES DOULEURS OCCULAIRES ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        douleur_oc = "POSITIF"
    else:
        douleur_oc = "NEGATIF"
    
    enquete_oph = {
        "Myodesopsies":myodesopsie,
        "Metamorpheries":metamorpherie,
        "Phospheres":phosphene,
        "Photophobie":photophobie,
        "Larmoiement":larmoiement,
        "Douleur Occulaire":douleur_oc
    }

    return enquete_oph



def Examen_oph():
    """ Cette methode definit les examens effectues sur la systeme ophtalmique """

    print(" INSPECTION DU SYSTEME OPHTALMIQUE \n")
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
    
    print(" PALPATION DU SYSTEME OPHTALMIQUE \n")
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
    
    print(" PERCUTION DU SYSTEME OPHTALMIQUE \n")
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

    print(" AUSCULTATION DU SYSTEME OPHTALMIQUE \n")
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

    examen_oph = {
        "Inspection du systeme ophtalmique":liste_inspection,
        "Palpation du systeme ophtalmique":liste_palpation,
        "Percution du systeme ophtalmique":liste_percution,
        "Auscultation du systeme ophtalmique":liste_auscultation
    }

    return examen_oph


