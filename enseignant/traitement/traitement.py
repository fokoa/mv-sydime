def Traitement():
    """ Cette méthode donne toutes les informations concernant le traitement du patient """

    print("PRESENTATION DU TRAITEMENT DU PATIENT \n")

    print("LES BUTS A ATTEINDRE ")
    ajouter_but = True
    buts = []

    while ajouter_but == True:

        but = input("INDIQUEZ UN BUT DU TRAITEMENT PRESCRIT AU PATIENT: ")
        
        buts.append(but)

        ajouter = input("Y A T-IL D'AUTRES BUTS A ATTEINDRE ?\n VEUILLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")
        if ajouter == 'O' or ajouter == 'o' :
            ajouter_but = True
        else:
            ajouter_but = False
    



    print("LES MESURES GENERALES")
    ajouter_mesure = True
    mesures = []

    while ajouter_mesure == True:

        mesure = input("INDIQUEZ UNE MESURE A PRENDRE: ")
        
        mesures.append(mesure)

        ajouter = input("Y A T-IL D'AUTRES MESURES ?\n VEUILLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")
        if ajouter == 'O' or ajouter == 'o' :
            ajouter_mesure = True
        else:
            ajouter_mesure = False
    



    print("LES MESURES GENERALES")
    ajouter_s = True
    mesures_sp = []

    while ajouter_s == True:

        medicament = input("INDIQUEZ LE MEDICAMENT A PRENDRE: ")

        posologie = input("INDIQUEZ LA POSOLOGIE : ")
        
        mesure = {
            "Le medicament":medicament,
            "Posologie":posologie
        }
        mesures_sp.append(mesure)

        ajouter = input("Y A T-IL D'AUTRES MEDICAMENTS ?\n VEUILLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")
        if ajouter == 'O' or ajouter == 'o' :
            ajouter_s = True
        else:
            ajouter_s = False

    


    print("SURVEILLANCES")
    ajouter_mesure = True
    surveillances = []

    while ajouter_mesure == True:

        type_s = input("INDIQUEZ LE TYPE DE SURVEILLANCES A EFFECTUER: ")

        ajouter_parametre = True
        parametres = []

        while ajouter_parametre == True:

            para = input("INDIQUEZ LE PARAMETRE A SURVEILLEZ: ")
            
            parametres.append(para)

            ajouter = input("Y A T-IL D'AUTRES PARAMETRE A SURVEILLER ?\n VEUILLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")
            if ajouter == 'O' or ajouter == 'o' :
                ajouter_parametre = True
            else:
                ajouter_parametre = False
        
        mesure = {
            "Type":type_s,
            "Parametres":parametres
        }

        surveillances.append(mesure)

        ajouter = input("Y A T-IL D'AUTRES MESURES ?\n VEUILLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")
        if ajouter == 'O' or ajouter == 'o' :
            ajouter_mesure = True
        else:
            ajouter_mesure = False
    

    print("PRONOSTIC")
    ajouter_pronostic = True
    pronostics = []

    while ajouter_pronostic == True:

        pronostic = input("PRESENTEZ UN PRONOSTIC POUR LE PATIENT: ")
        
        pronostics.append(pronostic)

        ajouter = input("Y A T-IL D'AUTRES PRONOSTIC ?\n VEUILLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")
        if ajouter == 'O' or ajouter == 'o' :
            ajouter_pronostic = True
        else:
            ajouter_pronostic = False

    
    traitement = {
        "Buts":buts,
        "Mesures generales":mesures,
        "Mesures specifiques":mesures_sp,
        "Surveillances":surveillances,
        "Pronostics":pronostics
    }

    return traitement