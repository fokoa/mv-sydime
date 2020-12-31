from genicologie.genico import *
from genicologie.ummino import *


# LA FONCTION DU SEXE DU PATIENT
def Sexe():
    """ Cette fonction permet de récuperer le sexe du patient"""
    sexe_car = " "
    while sexe_car != "F" and sexe_car != "f" and sexe_car !="M" and sexe_car !="m":
        sexe_car = input("VEUILLEZ INDIQUER LE SEXE DU PATIENT EN ENTRANT 'F' OU 'M' :")

        if sexe_car != "F" and sexe_car != "f" and sexe_car !="M" and sexe_car !="m":
                print("DESOLE LE CARACTERE ENTRE NE REPRESENTE PAS UN SEXE\n ")
                print("VEUILLEZ INDIQUER LE SEXE DU PATIENT EN ENTRANT 'F' OU 'M'\n ")
        elif sexe_car == "F" or sexe_car =="f":
            sexe = "Femme"
        elif sexe_car == "M" or sexe_car == "m":
            sexe = "Homme"

    return sexe


# LA FONCTION DU STATUS DU PATIENT
def Status():
    """ Cette fonction permet de récuperer le status matrimonial du patient"""
       
    print("VEUILLEZ INDIQUER LE STATUS DU PATIENT PARMIS LES STATUS CI-DESSOUS \n")
    print("\n")
    print(" 1-  MARIE \n")
    print(" 2-  FIANCE \n")
    print(" 3-  CELIBATAIRE \n")
    print(" 4-  AUTRE... \n")
    print("\n")

    choix = 0
    while choix <= 0 or choix > 7 :
        choix = input("HOISISSEZ LE STATUS DU PATIENT EN INDIQUANT JUSTE LE NUMERO SU STATUS : ")
        try :
            choix = int(choix)
        except ValueError :
            print("VOUS N'AVEZ PAS TAPE UN CHIFFRE MAIS PLUTOT UN MOT \n")
            choix = 0
        if choix < 0 :
            print("DESOLE MAIS LE NUMERO ENTRE NE FAIS PAS PARTIR DES CHOIX!  \n")
            print("VEUILLEZ CHOISIR PARMI LES NUMERO DE LA LISTE \n")
        elif choix > 7  :
            print("DESOLE LE CHOIX ENTRER NE FAIT PAS PARTIR DES CHOIX DEFINIT")

    if choix == 1:
        status = "MARIE"
    if choix == 2:
        status = "FIANCE"
    if choix == 3:
        status = "CELIBATAIRE"
    else:
        status = "AUTRE"

    return status


# LA FONCTION DU MODE DE VIE DU PATIENT
def mode_vie():
    """ Indique le mode de vie du patient """

    print("LE PATIENT A T-IL DES HABITUDES DE VIE? \n")

    reponse = input("REPONDEZ PAR 'O' POUR OUI OU 'n' POUR NON : ")

    if reponse == "N" or reponse == "n":
        description = "AUCUNES"
    elif reponse == "O" or reponse == "o":
        description = input("DECRIVEZ SES HABITUDES \n")
    
    ante_mode = {
        "Type":"MODE DE VIE",
        "Description":description
    }

    return ante_mode


# LA FONCTION DU STATUS MEDICALE DU PATIENT
def medicale():
    """ Indique les maladies incurables du patient"""

    liste   = []
    print("LE PATIENT A T-IL UNE MALADIE INCURABLE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "N" or reponse == "n" :
        if len(liste) == 0:
            liste.append("AUCUNE")
            
    elif reponse == "O" or reponse == "o":
        ajouter = True
        while ajouter == True:

            maladie = input("INDIQUEZ LA MALADIE DU PATIENT: ")
            liste.append(maladie)
            reponse = input("LA PATIENT A T-IL UNE AUTRE MALADIE ?\n VEUILLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")
            if reponse == 'O' or reponse == 'o' :
                ajouter = True
            else:
                ajouter = False

    ante_medi = {
        "Type":"ANTECEDENTS MEDICAUX",
        "Liste des maladies":liste
    }   

    return ante_medi        


# LA FONCTION DU STATUS CHIRUGICALE DU PATIENT
def chirugicale():
    """ Indique les maladies incurables du patient"""

    liste   = []
    print("LE PATIENT A T-IL SUBI UNE CHIRUGIE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "N" or reponse == "n" :
        if len(liste) == 0:
            liste.append("AUCUNE")
            

    elif reponse == "O" or reponse == "o":
        ajouter = True
        while ajouter == True:
            operation = input("INDIQUEZ LA CHIRUGIE SUBI PAR LE PATIENT: ")
            cause = input("INDIQUEZ LA CAUSE DE LA CHIRUGIE: ")
    
            chirugie = {
                "Chirugie subi":operation,
                "Raison de la chirugie":cause
            }
            liste.append(chirugie)

            reponse = input("LA PATIENT A T-IL UNE AUTRE MALADIE ?\n VEUILLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")
            if reponse == 'O' or reponse == 'o' :
                ajouter = True
            else:
                ajouter = False

    ante_chiru = {
        "Type":"ANTECEDENTS CHIRUGICAUX",
        "Liste des chirugies":liste
    }   

    return ante_chiru


# LA FONCTION DU STATUS IMMUNO-ALLERGIQUE DU PATIENT
def Immuno_allergique():
    """ cette méthode récupère les éléments ummino-allergique du aptient"""

    groupe_sanguin = Groupe_sanguin()
    rhesus = Facteur_rhesus()
    phoreze = Electrophoreze()
    serologie = Serologie()
    allergenes = Allergenes()

    ant_ummino = {
        "Type": "ANTECEDENT IMMUNO_ALLERGIQUE",
        "Groupe sanguin":groupe_sanguin,
        "Facteur rhesus":rhesus,
        "Electrophoreze":phoreze,
        "Serologie":serologie,
        "Allergenes du patient":allergenes
    }
    return ant_ummino



# LA FONCTION DU STATUS TOXICOLOGIQUE DU PATIENT
def Toxicologie():
    """ Cette méthode permet de définir la toxicologie du patient """

    reponse_tab = input("CONSOMMEZ-VOUS DU TABAC?\n VEUILLEZ REPONDRE PAR 'O' POUR OUI 'n' POUR NON : ")
    while reponse_tab !="O" and reponse_tab != "o" and reponse_tab != "N" and reponse_tab != "n":
        reponse_tab = input("LE CARACTERE ENTRE N'EST PAS UNE REPONSE\n VEUILLEZ ENTRE LES CARACTERES DE REPONSES INDIQUES CI-DESSUS \n")

    if reponse_tab == "O" or reponse_tab == "o":
        valt = "POSITIF"
    else:
        valt = "NEGATIF"
    
    reponse_dro = input("CONSOMMEZ-VOUS DE LA DROGUE?\n VEUILLEZ REPONDRE PAR 'O' POUR OUI 'n' POUR NON : ")
    while reponse_dro !="O" and reponse_dro != "o" and reponse_dro != "N" and reponse_dro != "n":
        reponse_dro = input("LE CARACTERE ENTRE N'EST PAS UNE REPONSE\n VEUILLEZ ENTRE LES CARACTERES DE REPONSES INDIQUES CI-DESSUS \n")

    if reponse_dro == "O" or reponse_dro == "o":
        vald = "POSITIF"
    else:
        vald = "NEGATIF"
    
    reponse_alc = input("CONSOMMEZ-VOUS DE L'ALCOOL?\n VEUILLEZ REPONDRE PAR 'O' POUR OUI 'n' POUR NON : ")
    while reponse_alc !="O" and reponse_alc != "o" and reponse_alc != "N" and reponse_alc != "n":
        reponse_alc = input("LE CARACTERE ENTRE N'EST PAS UNE REPONSE\n VEUILLEZ ENTRE LES CARACTERES DE REPONSES INDIQUES CI-DESSUS \n")

    if reponse_alc == "O" or reponse_alc == "o":
        vala = "POSITIF"
    else:
        vala = "NEGATIF"

    
    reponse_phar = input("CONSOMMEZ-VOUS DES PRODUITS DE LA PHARMACOPE?\n VEUILLEZ REPONDRE PAR 'O' POUR OUI 'n' POUR NON : ")
    while reponse_phar !="O" and reponse_phar != "o" and reponse_phar != "N" and reponse_phar != "n":
        reponse_phar = input("LE CARACTERE ENTRE N'EST PAS UNE REPONSE\n VEUILLEZ ENTRE LES CARACTERES DE REPONSES INDIQUES CI-DESSUS \n")

    if reponse_phar == "O" or reponse_phar == "o":
        valp = "POSITIF"
    else:
        valp = "NEGATIF"
    
    ante_toxi = {
        "Consommation de Tabac":valt,
        "Consommation de Drogue":vald,
        "Consommation d'Alcool":vala,
        "CConsommation des produits de Pharmacope":valp
    }
    return ante_toxi


# LA FONCTION DU STATUS FAMILIALE DU PATIENT
def Familiaux():
    """ Indique l'etat de santé des personnes proches du patient """

    liste   = []
    print("LE PATIENT A T-IL AVEC DES PROCHE ?")
    reponse = input(" VEULLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")

    if reponse == "N" or reponse == "n" :
        if len(liste) == 0:
            liste.append("AUCUNE")
            
    elif reponse == "O" or reponse == "o":
        ajouter = True
    
        while ajouter == True:
            personne = input("INDIQUEZ LA PERSONNE : ")
            description= input("DONNEZ UNE DESCRIPTION DE L'ETAT DE SANTE DE LA PERSONNE : ")
            proche = {
                "Nom":personne,
                "Description": description
            }
            liste.append(proche)

            reponse = input("LA PATIENT A T-IL UNE D'AUTRE PROCHE?\n VEUILLEZ REPONDRE PAR 'O' POUR OUI ET 'n' POUR NON : ")
            if reponse == 'O' or reponse == 'o' :
                ajouter = True
            else:
                ajouter = False
    
    ante_familial = {
        "Type":"ANTECEDENTS FAMILIAUX",
        "Liste des proches du patient":liste
    }

    return ante_familial


# LA FONCTION DU STATUS GENICO-OBSTETRIQUE DU PATIENT
def Genico_obs(sexe):
    """ Cette méthode permet de returner les antécédents génico_obstétriques d'un patient"""

    if sexe == "Femme":
        maladies_genico = maladie_genicologique()
        nombre_gross = nb_grossesse()
        nombre_comp = complication()
        nombre_fausse = fausse_couche()
        maladie_grossesse = maladi_grossesse()
        ante_genico = {
            "TYPE":"ANTECEDENT GENICO-OBSTETRIQUE",
            "Maladies genicologiques":maladies_genico,
            "Nombre de grossesses": nombre_gross,
            "Nombre de complication de grossesse": nombre_comp, 
            "Nombre de fausse couches": nombre_fausse,
            "Maladies de grossesses":maladie_grossesse
        }

        return ante_genico
    else:
        maladies_genico = maladie_genicologique()
        ante_genico = {
            "TYPE":"ANTECEDENT GENICO-OBSTETRIQUE",
            "Maladies genicologiques":maladies_genico
        }

        return ante_genico
   

