def systeme_endo():
    """ permet de récuperer les enquetes sur le systeme endocrinologique des patient"""

    print("\n")
    print("SYSTEME ENDOCRINOLOGIQUE\n")
    
    # POUR LA POLYDYSIE
    print("LE PATIENTE A T-IL DE LA POLYDYSIE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        polydysie = "POSITIF"
    else:
        polydysie = "NEGATIF"

    # POUR L'AMAIGRISSEMENT
    print("LE PATIENTE EST T-IL MAIGRE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        ammaigrissement = "POSITIF"
    else:
        ammaigrissement ="NEGATIF"

    # POUR L'HYPERSUDATION
    print("LE PATIENTE A T-IL DE L'HYPERSUDATION ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        hypersudation = "POSITIF"
    else:
        hypersudation = "NEGATIF"

    # POUR LA POLYURIE
    print("LE PATIENTE A T-IL DE LA POLYURIE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        polyurie = "POSITIF"
    else:
        polyurie = "NEGATIF"
    
    enquete_endo = {
        "Polydysie":polydysie,
        "Amaigrissement":ammaigrissement,
        "Hypersudation":hypersudation,
        "Polyurie":polyurie
    }

    return enquete_endo
    

def Examen_endo():
    """ Cette methode definit les examens effectues sur le systeme endocrinologique """

    print(" INSPECTION DU SYSTEME ENDOCRINOLOGIQUE \n")
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

    print(" PALPATION DU SYSTEME ENDOCRINOLOGIQUE \n")
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

    print(" PERCUTION DU SYSTEME ENDOCRINOLOGIQUE \n")
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

    print(" AUSCULTATION DU SYSTEME ENDOCRINOLOGIQUE \n")
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

    examen_endo= {
        "Inspection du systeme endocrinologique":liste_inspection,
        "Palpation du systeme endocrinologique":liste_palpation,
        "Percution du systeme endocrinologique":liste_percution,
        "Auscultation du systeme endocrinologique":liste_auscultation
    }

    return examen_endo

