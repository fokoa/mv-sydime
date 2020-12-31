def Complementaire():
    """ cette methode nous permetra de definir les examens complementaires du patient """

    liste_exam = []
    print("Y A T-IL DES EXAMENS D'AVISE DE DIAGNOSTIC A PRISCRIRE AU PATIENT ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "N" or reponse == "n" :
        if len(liste_exam) == 0:
            liste_exam.append("AUCUNE")

    elif reponse == "O" or reponse == "o":
        ajouter_exam = True
        while ajouter_exam == True:
            avise = input("VEUILLEZ INDIQUER L' EXAMEN \n")
            liste_exam.append(avise)
            rajouter = input("Y A T-IL D'AUTRES EXAMEN? REPONDEZ PAR 'O' POUR OUI ET 'n' POUR NON : ")
            if rajouter == 'O' or rajouter == 'o':
                ajouter_exam = True
            else:
                ajouter_exam = False

    liste_reten = []
    print("Y A T-IL DES EXAMENS DE RETENTISSEMENT A PRISCRIRE AU PATIENT ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "N" or reponse == "n" :
        if len(liste_reten) == 0:
            liste_reten.append("AUCUNE")

    elif reponse == "O" or reponse == "o":
        ajouter_exam = True
        while ajouter_exam == True:
            retenti = input("VEUILLEZ INDIQUER L' EXAMEN \n")
            liste_reten.append(retenti)
            rajouter = input("Y A T-IL D'AUTRES EXAMEN? REPONDEZ PAR 'O' POUR OUI ET 'n' POUR NON : ")
            if rajouter == 'O' or rajouter == 'o':
                ajouter_exam = True
            else:
                ajouter_exam = False

    liste_ter = []
    print("Y A T-IL DES EXAMENS DE TERRAIN A PRISCRIRE AU PATIENT ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "N" or reponse == "n" :
        if len(liste_ter) == 0:
            liste_ter.append("AUCUNE")
            
    elif reponse == "O" or reponse == "o":
        ajouter_exam = True
        while ajouter_exam == True:
            terrain = input("VEUILLEZ INDIQUER L' EXAMEN \n")
            liste_ter.append(terrain)
            rajouter = input("Y A T-IL D'AUTRES EXAMEN? REPONDEZ PAR 'O' POUR OUI ET 'n' POUR NON : ")
            if rajouter == 'O' or rajouter == 'o':
                ajouter_exam = True
            else:
                ajouter_exam = False
    
    complementaire = {
        "Avise de diagnostic":liste_exam,
        "Retentissement":liste_reten,
        "Terrain":liste_ter
    }

    return complementaire
