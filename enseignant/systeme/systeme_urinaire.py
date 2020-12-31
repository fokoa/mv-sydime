def systeme_urinaire():
    """ permet de récuperer les enquetes sur le systeme nerveux des patient"""

    print("\n")
    print("SYSTEME URINAIRE\n")
    
    # POUR L'ANURIE
    print("LE PATIENTE A T-IL DE L'ANURIE?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        anurie = "POSITIF"
    else:
        anurie = "NEGATIF"    

    # POUR L'ALLIGURIE
    print("LE PATIENTE A T-IL DE L'ALLIGURIE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        alligurie = "POSITIF"
    else:
        alligurie = "NEGATIF"
    
    # POUR LA POLYURIE
    print("LE PATIENTE A T-IL DE LA POLYURIE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        polyurie = "POSITIF"
    else:
        polyurie = "NEGATIF"

    # POUR LA NYCHURIE
    print("LE PATIENTE A T-IL DE LA NYCHURIE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        nychurie = "POSITIF"
    else:
        nychurie = "NEGATIF"
    
    # POUR LA DYSURIE
    print("LE PATIENTE A T-IL DE LA DYSURIE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        dysurie = "POSITIF"
    else:
        dysurie = "NEGATIF"
    
    # POUR LES BRULLURES MICHRONNELLES
    print("LE PATIENTE A T-IL DES BRULLURES MICHRONNELLES ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        brullures = "POSITIF"
    else:
        brullures = "NEGATIF"
    
    # POUR L'HEMATURIE
    print("LE PATIENTE A T-IL DE L'HEMATURIE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        hematurie = "POSITIF"
    else:
        hematurie = "NEGATIF"
    
    # POUR LA CHYLURIE
    print("LE PATIENTE A T-IL DE LA CHYLURIE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        chylurie = "POSITIF"
    else:
        chylurie = "NEGATIF"
    
    # POUR LA PYURIE
    print("LE PATIENTE A T-IL DE LA PYURIE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        pyurie = "POSITIF"
    else:
        pyurie = "NEGATIF"

    enquete_urinaire ={
        "Anurie":anurie,
        "Alligurie":alligurie,
        "Polyurie":polyurie,
        "Nychurie":nychurie,
        "Dysurie":dysurie,
        "Brullures Michronnelle":brullures,
        "Hematurie":hematurie,
        "Chylurie":chylurie,
        "Pyurie":pyurie
    }

    return enquete_urinaire



def Examen_urinaire():
    """ Cette methode definit les examens effectues sur le systeme urinaire """

    print(" INSPECTION DU SYSTEME URINAIRE \n")
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

    print(" PALPATION DU SYSTEME URINAIRE \n")
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
    
    print(" PERCUTION DU SYSTEME URINAIRE \n")
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

    examen_urinaire = {
        "Inspection du systeme urinaire":liste_inspection,
        "Palpation du systeme urinaire":liste_palpation,
        "Percution du systeme urinaire":liste_percution,
        "Auscultation du systeme urinaire":liste_auscultation
    }

    return examen_urinaire   


    