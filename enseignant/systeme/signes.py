def signes():
    """ permet de récuperer les signes généraux des patient"""

    # POUR L'ASTHENIE
    print("LE PATIENTE A T-IL DE LA FATIGUE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        asthenie = "POSITIF"
    else:
        asthenie = "NEGATIF"

    # POUR L'ANOREXIE
    print("LE PATIENTE A T-IL DE L'APPETIE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        anorexie = "POSITIF"
    else:
        anorexie ="NEGATIF"

    # POUR L'AMMAIGRISSEMENT
    print("LE PATIENTE EST T-IL MAIGRE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        ammaigrissement = "POSITIF"
    else:
        ammaigrissement ="NEGATIF"

    # POUR LA SUEUR
    print("LE PATIENTE SUE T-IL ABONDAMMENT ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        sueurs = "POSITIF"
    else:
        sueurs = "NEGATIF"
    
    # POUR LES FRISSONS
    print("LE PATIENTE FRISSONNE T-IL  ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        frissons = "POSITIF"
    else:
        frissons = "NEGATIF"

    # POUR LA SOIF
    print("LE PATIENTE A T-IL SOIF ABONDAMMENT ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        soif = "POSITIF"
    else:
        soif = "NEGATIF"
    
    # POUR LA FIEVRE
    print("LE PATIENTE A T-IL DE LA FIEVRE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        fievre = "POSITIF"
    else:
        fievre = "NEGATIF"
    
    # POUR LA PRURIT
    print("LE PATIENTE A T-IL DE LA PRURIT ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "O" or reponse == "o":
        prurit = "POSITIF"
    else:
        prurit ="NEGATIF"
    
    signe = {
        "Asthenie":asthenie,
        "Amaigrissement":ammaigrissement,
        "Anorexie":anorexie,
        "Fievre":fievre,
        "Sueurs":sueurs,
        "Frissosn":frissons,
        "Soif":soif,
        "Pruri":prurit
    }

    return signe

